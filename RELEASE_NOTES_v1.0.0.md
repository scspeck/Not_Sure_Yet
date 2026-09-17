# Trait MMAP v1.0.0

Final feature pass built from v0.2.5, preserving prior fixes.

## Preserved fixes
- Categorical filters are inactive when `All values` is selected.
- A selected categorical value is strict and excludes missing/nonmatching values.
- Numeric traits have exact/min/max filtering independent of `Size by`.
- Ecoregions are non-interactive and cannot intercept specimen clicks.
- Ecoregions load by visible map extent and remain below specimen points.
- Popup field labels and values remain separated.

## v1.0 additions
- Toggleable marker clustering with chunked loading.
- Toggleable record-density heatmap.
- Zoom to filtered records.
- Rectangle and polygon spatial selection.
- Scale bar.
- Live cursor coordinates.
- Full-screen map control.
- Place-name navigation search.
- Filtered/selected GeoJSON export in addition to CSV.
- Active-filter summary with visible/mappable counts.
- Existing global terrestrial ecoregion reference overlay retained.

Record-density heatmaps represent mapped record density, not organism abundance.
