# Trait MMAP

**Trait MMAP (Mapper for Mammals and Parasites)** is an upload-first, browser-based research mapping tool for rapid spatial exploration of mammal, parasite, museum-specimen, locality, and trait datasets.

Researchers upload a CSV, map coordinate and descriptive fields, classify arbitrary columns as numeric, categorical, or text traits, filter records, inspect and spatially select observations, visualize record density, and export subsets as CSV or GeoJSON.

## Core workflow
1. Upload a CSV or load the bundled example.
2. Map latitude, longitude, taxonomy, date, geography, and other fields.
3. Select additional numeric, categorical, or text traits.
4. Build the map.
5. Filter, search, cluster, inspect, or spatially select records.
6. Export filtered or selected records as CSV or GeoJSON.

## Major features
- Flexible upload-first CSV workflow.
- Exact categorical and numeric exact/minimum/maximum filtering.
- Unit-tolerant numeric parsing while preserving original exported values.
- Marker clustering and record-density heatmap.
- Left-click inspection and right-click individual selection.
- Rectangle and polygon spatial selection.
- CSV and GeoJSON export.
- Active-filter summary and zoom-to-filtered.
- Scale bar, cursor coordinates, full-screen view, and place navigation.
- Optional RESOLVE terrestrial ecoregion reference overlay.

## Running locally
Serve the repository rather than opening `index.html` as a `file://` page:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Minimum input
Valid latitude and longitude are required for a row to be mappable. Other fields are optional and mapped by the user. See `docs/DATA_FORMAT.md`.

## Scientific interpretation
Trait MMAP visualizes records; it does not infer abundance, occupancy, causation, or ecological association. Spatial density can reflect collecting effort, digitization history, missing data, spatial bias, or biology. The heatmap represents **mapped record density, not organism abundance**.

## Validation and documentation
A controlled regression dataset is in `examples/`. See `docs/TESTING.md`, `docs/USER_GUIDE.md`, `docs/DATA_FORMAT.md`, `docs/DATA_SOURCES.md`, and `docs/MAINTENANCE.md`.

## Citation
Citation metadata are provided in `CITATION.cff`. Add the archival DOI after v1.0.0 is deposited.

## License
MIT. See `LICENSE`.

## Release status
Version 1.0.0 is the publication-oriented release candidate. Complete `RELEASE_CHECKLIST.md` before tagging the archival release.
