---
search:
  boost: 5.0
---

# Slot: has_deployment_location 


_Specifies the location of technology deployment and use_



<div data-search-exclude markdown="1">



URI: [tech:has_deployment_location](https://w3id.org/lmodel/dpv/tech/has_deployment_location)
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


* has deployment location




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasDeploymentLocation |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_deployment_location |
| native | tech:has_deployment_location |
| exact | dpv_tech:hasDeploymentLocation, dpv_tech_owl:hasDeploymentLocation |




## LinkML Source

<details>
```yaml
name: has_deployment_location
definition_uri: tech:hasDeploymentLocation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasDeploymentLocation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Specifies the location of technology deployment and use
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has deployment location
exact_mappings:
- dpv_tech:hasDeploymentLocation
- dpv_tech_owl:hasDeploymentLocation
rank: 1000
range: string
multivalued: true

```
</details></div>