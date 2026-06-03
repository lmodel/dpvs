---
search:
  boost: 5.0
---

# Slot: has_intended_use 


_Indicates the intended use of technology_



<div data-search-exclude markdown="1">



URI: [tech:has_intended_use](https://w3id.org/lmodel/dpv/tech/has_intended_use)
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


* has intended use




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasIntendedUse |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_intended_use |
| native | tech:has_intended_use |
| exact | dpv_tech:hasIntendedUse, dpv_tech_owl:hasIntendedUse |




## LinkML Source

<details>
```yaml
name: has_intended_use
definition_uri: tech:hasIntendedUse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasIntendedUse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the intended use of technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has intended use
exact_mappings:
- dpv_tech:hasIntendedUse
- dpv_tech_owl:hasIntendedUse
rank: 1000
range: string
multivalued: true

```
</details></div>