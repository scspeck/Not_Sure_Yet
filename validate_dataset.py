#!/usr/bin/env python3
"""
Trait MMAP optional dataset validator.

This script is NOT required to use Trait MMAP. Trait MMAP itself reads CSV files
directly in the browser. This helper is intended for maintainers or researchers
who want a reproducible preflight check for large datasets before upload.

Example:
    python scripts/validate_dataset.py data.csv --lat DEC_LAT --lon DEC_LONG \
        --scientific-name SCIENTIFIC_NAME --date VERBATIM_DATE
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
from collections import Counter
from pathlib import Path


YEAR_RE = re.compile(r"\b((?:17|18|19|20|21)\d{2})\b")


def finite_number(value: str):
    value = (value or "").strip().replace(",", "")
    if not value:
        return None
    try:
        n = float(value)
    except ValueError:
        return None
    return n if math.isfinite(n) else None


def parse_year(value: str):
    value = (value or "").strip()
    if not value:
        return None
    match = YEAR_RE.search(value)
    return int(match.group(1)) if match else None


def main():
    p = argparse.ArgumentParser(description="Validate a CSV before loading it into Trait MMAP.")
    p.add_argument("csv_file", type=Path)
    p.add_argument("--lat", required=True, help="Latitude column name")
    p.add_argument("--lon", required=True, help="Longitude column name")
    p.add_argument("--scientific-name", help="Scientific-name column")
    p.add_argument("--date", help="Date/year column")
    p.add_argument("--encoding", default="utf-8-sig")
    p.add_argument("--json-out", type=Path, help="Optional JSON summary output")
    args = p.parse_args()

    total = 0
    valid = 0
    invalid = 0
    years = []
    taxa = Counter()

    with args.csv_file.open("r", encoding=args.encoding, newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise SystemExit("No CSV header row was detected.")

        missing = [c for c in [args.lat, args.lon, args.scientific_name, args.date] if c and c not in reader.fieldnames]
        if missing:
            raise SystemExit("Missing requested columns: " + ", ".join(missing))

        for row in reader:
            total += 1
            lat = finite_number(row.get(args.lat, ""))
            lon = finite_number(row.get(args.lon, ""))
            ok = lat is not None and lon is not None and -90 <= lat <= 90 and -180 <= lon <= 180
            if ok:
                valid += 1
            else:
                invalid += 1

            if args.date:
                y = parse_year(row.get(args.date, ""))
                if y is not None:
                    years.append(y)

            if args.scientific_name:
                name = (row.get(args.scientific_name, "") or "").strip()
                if name:
                    taxa[name] += 1

    summary = {
        "file": str(args.csv_file),
        "rows": total,
        "valid_coordinate_rows": valid,
        "invalid_coordinate_rows": invalid,
        "coordinate_completeness_percent": round(100 * valid / total, 2) if total else 0,
        "year_min": min(years) if years else None,
        "year_max": max(years) if years else None,
        "unique_scientific_names": len(taxa) if args.scientific_name else None,
        "most_common_scientific_names": taxa.most_common(10) if args.scientific_name else None,
    }

    print(json.dumps(summary, indent=2))
    if args.json_out:
        args.json_out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        print(f"\nWrote summary to {args.json_out}")


if __name__ == "__main__":
    main()
