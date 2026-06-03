---
search:
  boost: 5.0
---

# Slot: iso_numeric 


_The ISO-Numeric code for a given region_



<div data-search-exclude markdown="1">



URI: [loc:iso_numeric](https://w3id.org/lmodel/dpv/loc/iso_numeric)
<!-- no inheritance hierarchy -->







## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |






## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ISO-numeric




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#iso_numeric |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:iso_numeric |
| native | loc:iso_numeric |
| exact | dpv_loc:iso_numeric, dpv_loc_owl:iso_numeric |




## LinkML Source

<details>
```yaml
name: iso_numeric
definition_uri: loc:iso_numeric
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#iso_numeric
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: The ISO-Numeric code for a given region
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ISO-numeric
exact_mappings:
- dpv_loc:iso_numeric
- dpv_loc_owl:iso_numeric
rank: 1000
range: string
multivalued: true

```
</details></div>