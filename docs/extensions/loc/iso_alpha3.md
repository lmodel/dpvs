---
search:
  boost: 5.0
---

# Slot: iso_alpha3 


_The ISO-Alpha3 code for a given region_



<div data-search-exclude markdown="1">



URI: [loc:iso_alpha3](https://w3id.org/lmodel/dpv/loc/iso_alpha3)
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


* ISO-alpha3




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#iso_alpha3 |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:iso_alpha3 |
| native | loc:iso_alpha3 |
| exact | dpv_loc:iso_alpha3, dpv_loc_owl:iso_alpha3 |




## LinkML Source

<details>
```yaml
name: iso_alpha3
definition_uri: loc:iso_alpha3
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#iso_alpha3
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: The ISO-Alpha3 code for a given region
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ISO-alpha3
exact_mappings:
- dpv_loc:iso_alpha3
- dpv_loc_owl:iso_alpha3
rank: 1000
range: string
multivalued: true

```
</details></div>