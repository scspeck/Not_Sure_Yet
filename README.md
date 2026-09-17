# Trait MMAP-Mapper for Mammals and Parasites

This branch/package changes Trait MMAP from a static hosted-data atlas into an **upload-first research tool**.

## What changed

- No `tracker.json` is required at page load.
- The landing workflow begins with a user CSV upload.
- Users explicitly map latitude/longitude and optional ID, taxon, date, geography, and locality fields.
- Trait MMAP infers potential trait types and lets the user choose which columns become filters.
- Numeric traits generate min/max filters.
- Categorical traits generate value filters.
- Text traits generate contains-search filters.
- The map can color points by a categorical trait and size points by a numeric trait.
- Left-click inspects a record.
- Right-click selects/deselects a record.
- Polygon selection selects all currently visible points inside the polygon.
- Filtered and selected downloads preserve all original CSV columns.
- Uploaded data remain client-side in the browser session.
- A small example dataset is embedded in the application and also provided under `examples/`.

## Deploy

The app is static. Upload `index.html` to the root of a GitHub Pages repository and deploy it normally.

No Python process, database, static dataset, or API key is required for ordinary use.

## Optional validation

For a large research dataset, run:

```bash
python scripts/validate_dataset.py your_data.csv --lat DEC_LAT --lon DEC_LONG --scientific-name SCIENTIFIC_NAME --date VERBATIM_DATE
```

This helper reports coordinate completeness, year range, and basic taxonomic counts. It does not transform the original data.

## Important architectural point

Source-specific integrations (Arctos, GBIF, institutional APIs, etc.) should be implemented later as **optional import adapters** that produce the same tabular input model used by the upload workflow. Trait MMAP itself should remain usable without an account or API key.
