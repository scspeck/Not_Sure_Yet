# Release and regression testing

Before each tagged release, load `examples/trait_mmap_validation.csv` and compare results with `examples/EXPECTED_RESULTS.md`.

## Functional checklist
- CSV and bundled example load.
- Missing/invalid coordinates are excluded from mappable count.
- With no filters, visible equals mappable.
- `All values` does not remove missing categorical values.
- Specific categorical selections are strict.
- Numeric exact/min/max filters work independently of `Size by`.
- Unit-bearing numbers filter correctly without altering export values.
- Combined filters intersect correctly.
- Year and global search work.
- Left-click popup and right-click selection work.
- Ecoregions never block specimen interaction, including after toggling off.
- Rectangle and polygon selection work.
- Clustering and heatmap work on currently filtered records.
- Zoom-to-filtered works.
- Filtered/selected CSV and GeoJSON exports contain expected records.
- Scale, coordinates, full screen, and place navigation work.

## Performance smoke test
Test roughly 100, 1,000, 10,000, and 20,000+ mappable rows where possible. Record browser/version, OS, row count, mappable count, time to usable map, cluster behavior, filter responsiveness, and export success.

## Browser matrix
At minimum test current Chrome/Edge and Firefox; test Safari when available.

Keep a release issue or testing record with version, date, tester, browser, validation counts, known failures, and approval status.
