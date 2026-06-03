---
search:
  boost: 5.0
---

# Slot: has_application 


_Indicates the technology has or uses the associated application_



<div data-search-exclude markdown="1">



URI: [tech:has_application](https://w3id.org/lmodel/dpv/tech/has_application)
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


* has application




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasApplication |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_application |
| native | tech:has_application |
| exact | dpv_tech:hasApplication, dpv_tech_owl:hasApplication |




## LinkML Source

<details>
```yaml
name: has_application
definition_uri: tech:hasApplication
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasApplication
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated application
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has application
exact_mappings:
- dpv_tech:hasApplication
- dpv_tech_owl:hasApplication
rank: 1000
range: string
multivalued: true

```
</details></div>