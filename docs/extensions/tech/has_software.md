---
search:
  boost: 5.0
---

# Slot: has_software 


_Indicates the technology has or uses the associated software_



<div data-search-exclude markdown="1">



URI: [tech:has_software](https://w3id.org/lmodel/dpv/tech/has_software)
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


* [TechSubset](TechSubset.md)



## Aliases


* has software




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasSoftware |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_software |
| native | tech:has_software |
| exact | dpv_tech:hasSoftware, dpv_tech_owl:hasSoftware |




## LinkML Source

<details>
```yaml
name: has_software
definition_uri: tech:hasSoftware
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasSoftware
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated software
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has software
exact_mappings:
- dpv_tech:hasSoftware
- dpv_tech_owl:hasSoftware
rank: 1000
range: string
multivalued: true

```
</details></div>