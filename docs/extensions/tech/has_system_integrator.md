---
search:
  boost: 5.0
---

# Slot: has_system_integrator 


_Indicates technology system integrator_



<div data-search-exclude markdown="1">



URI: [tech:has_system_integrator](https://w3id.org/lmodel/dpv/tech/has_system_integrator)

## Inheritance

* [has_actor](has_actor.md)
    * **has_system_integrator**








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


* has system integrator




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasSystemIntegrator |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_system_integrator |
| native | tech:has_system_integrator |
| exact | dpv_tech:hasSystemIntegrator, dpv_tech_owl:hasSystemIntegrator |




## LinkML Source

<details>
```yaml
name: has_system_integrator
definition_uri: tech:hasSystemIntegrator
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasSystemIntegrator
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology system integrator
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has system integrator
exact_mappings:
- dpv_tech:hasSystemIntegrator
- dpv_tech_owl:hasSystemIntegrator
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>