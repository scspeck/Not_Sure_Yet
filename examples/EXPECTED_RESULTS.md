# Expected regression results

The validation CSV has **20 source rows**. `T016` has no coordinates and `T017` has invalid latitude, so **18 records are mappable**.

| Test | Expected |
|---|---:|
| No active filters | 18 visible |
| Genus = Myotis | 7 |
| Genus = Geomys | 3 |
| Genus = Myotis + State = Kansas | 5 |
| State = Kansas | 14 |
| Weight 10–20 | 4 |
| Weight ≥100 | 4 |
| Year ≥2022 | 5 |
| Search `Ixodes` | 1 |
| Genus = Myotis + Weight ≥10 | 3 |

Critical edge cases: `T013` has a Myotis scientific name but blank genus and must not pass `Genus=Myotis`; `T015` has missing weight and must not pass an active weight filter; `T002` and `T019` test unit-bearing numeric parsing.
