# Changelog

## [1.0.0] - 2026-09-17
First publication-oriented release candidate.

### Added
Upload-first CSV mapping; flexible numeric/categorical/text traits; numeric exact/min/max filtering; marker clustering; record-density heatmap; right-click, rectangle, and polygon selection; CSV/GeoJSON export; active-filter summary; zoom-to-filtered; scale, coordinates, full-screen mode, place navigation; and optional terrestrial ecoregions.

### Fixed before 1.0
- `All values` no longer excludes records with missing categorical fields.
- Specific categorical selections are strict.
- Numeric traits remain searchable filters independent of `Size by`.
- Ecoregions no longer intercept specimen interactions.
- Ecoregion requests are viewport-limited and simplified.
- Popup field labels and values are separated.

### Known limitations
Optional external services can be slow/unavailable. Browser performance varies with dataset size and hardware. Trait MMAP does not correct sampling bias or georeferencing errors.
