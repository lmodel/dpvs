---
search:
  boost: 5.0
---

# Slot: has_documentation 


_Indicates documentation associated with technology_



<div data-search-exclude markdown="1">



URI: [tech:has_documentation](https://w3id.org/lmodel/dpv/tech/has_documentation)
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


* has documentation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasDocumentation |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_documentation |
| native | tech:has_documentation |
| exact | dpv_tech:hasDocumentation, dpv_tech_owl:hasDocumentation |




## LinkML Source

<details>
```yaml
name: has_documentation
definition_uri: tech:hasDocumentation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasDocumentation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates documentation associated with technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has documentation
exact_mappings:
- dpv_tech:hasDocumentation
- dpv_tech_owl:hasDocumentation
rank: 1000
range: string
multivalued: true

```
</details></div>