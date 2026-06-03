---
search:
  boost: 5.0
---

# Slot: has_service 


_Indicates the technology has or uses the associated service_



<div data-search-exclude markdown="1">



URI: [tech:has_service](https://w3id.org/lmodel/dpv/tech/has_service)
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


* has service




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasService |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_service |
| native | tech:has_service |
| exact | dpv_tech:hasService, dpv_tech_owl:hasService |




## LinkML Source

<details>
```yaml
name: has_service
definition_uri: tech:hasService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated service
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has service
exact_mappings:
- dpv_tech:hasService
- dpv_tech_owl:hasService
rank: 1000
range: string
multivalued: true

```
</details></div>