---
search:
  boost: 5.0
---

# Slot: has_deployer 


_Indicates technology deployer_



<div data-search-exclude markdown="1">



URI: [tech:has_deployer](https://w3id.org/lmodel/dpv/tech/has_deployer)

## Inheritance

* [has_actor](has_actor.md)
    * **has_deployer**








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


* has deployer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasDeployer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_deployer |
| native | tech:has_deployer |
| exact | dpv_tech:hasDeployer, dpv_tech_owl:hasDeployer |




## LinkML Source

<details>
```yaml
name: has_deployer
definition_uri: tech:hasDeployer
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasDeployer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology deployer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has deployer
exact_mappings:
- dpv_tech:hasDeployer
- dpv_tech_owl:hasDeployer
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>