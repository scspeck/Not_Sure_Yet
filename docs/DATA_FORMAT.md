# Data format

Trait MMAP accepts CSV files with one header row and one record per subsequent row.

## Required for mapping
Map a **latitude** column (-90 to 90 decimal degrees) and **longitude** column (-180 to 180). Rows without valid coordinates remain source rows but are not mappable.

## Recommended fields
Scientific name, genus, species, family, country, state/province, county, locality, date/year, sex, life stage, stable specimen identifier/GUID, collection, parasite taxon, and measurements are useful but optional.

## Trait types
**Numeric:** measurements/counts; provides exact/min/max filtering and may also drive point size. A single numeric token can be parsed from values such as `23.4 g` or `151 mm`; the original source value is preserved in export.

**Categorical:** discrete values such as genus, sex, state, host species, or parasite family. `All values` is inactive. Selecting a category is strict: blanks and nonmatching values are excluded.

**Text:** free-form locality, remarks, reproductive notes, or association notes; uses contains-search behavior.

## Missing values
Inactive filters do not remove records merely because a trait is missing. Active categorical/numeric criteria exclude nonmatching or missing values according to the interface.

## Associations
Trait MMAP does not require one host–parasite schema. If one-to-many associations are flattened or aggregated before upload, document that transformation.

## Coordinate caution
Trait MMAP maps coordinates as supplied; it does not validate datum, uncertainty, locality consistency, or sensitive-species generalization.
