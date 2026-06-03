---
search:
  boost: 5.0
---

# Slot: has_provision_status 


_Indicates whether the technology has been provided_



<div data-search-exclude markdown="1">



URI: [tech:has_provision_status](https://w3id.org/lmodel/dpv/tech/has_provision_status)
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


* has provision status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasProvisionStatus |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_provision_status |
| native | tech:has_provision_status |
| exact | dpv_tech:hasProvisionStatus, dpv_tech_owl:hasProvisionStatus |




## LinkML Source

<details>
```yaml
name: has_provision_status
definition_uri: tech:hasProvisionStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasProvisionStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates whether the technology has been provided
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has provision status
exact_mappings:
- dpv_tech:hasProvisionStatus
- dpv_tech_owl:hasProvisionStatus
rank: 1000
range: string
multivalued: true

```
</details></div>