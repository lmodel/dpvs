---
search:
  boost: 5.0
---

# Slot: has_provision_method 


_Specifies the provision or usage method of technology_



<div data-search-exclude markdown="1">



URI: [tech:has_provision_method](https://w3id.org/lmodel/dpv/tech/has_provision_method)
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


* has provision method




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasProvisionMethod |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_provision_method |
| native | tech:has_provision_method |
| exact | dpv_tech:hasProvisionMethod, dpv_tech_owl:hasProvisionMethod |




## LinkML Source

<details>
```yaml
name: has_provision_method
definition_uri: tech:hasProvisionMethod
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasProvisionMethod
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Specifies the provision or usage method of technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has provision method
exact_mappings:
- dpv_tech:hasProvisionMethod
- dpv_tech_owl:hasProvisionMethod
rank: 1000
range: string
multivalued: true

```
</details></div>