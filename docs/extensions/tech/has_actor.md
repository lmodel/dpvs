---
search:
  boost: 5.0
---

# Slot: has_actor 


_Indicates an actor associated with technology_



<div data-search-exclude markdown="1">



URI: [tech:has_actor](https://w3id.org/lmodel/dpv/tech/has_actor)

## Inheritance

* **has_actor**
    * [has_auditor](has_auditor.md)
    * [has_customer](has_customer.md)
    * [has_deployer](has_deployer.md)
    * [has_designer](has_designer.md)
    * [has_developer](has_developer.md)
    * [has_evaluator](has_evaluator.md)
    * [has_installer](has_installer.md)
    * [has_maintainer](has_maintainer.md)
    * [has_manufacturer](has_manufacturer.md)
    * [has_owner](has_owner.md)
    * [has_partner](has_partner.md)
    * [has_producer](has_producer.md)
    * [has_provider](has_provider.md)
    * [has_purchaser](has_purchaser.md)
    * [has_subject](has_subject.md)
    * [has_supplier](has_supplier.md)
    * [has_system_integrator](has_system_integrator.md)
    * [has_user](has_user.md)








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


* has actor




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasActor |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_actor |
| native | tech:has_actor |
| exact | dpv_tech:hasActor, dpv_tech_owl:hasActor |




## LinkML Source

<details>
```yaml
name: has_actor
definition_uri: tech:hasActor
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasActor
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates an actor associated with technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has actor
exact_mappings:
- dpv_tech:hasActor
- dpv_tech_owl:hasActor
rank: 1000
range: string
multivalued: true

```
</details></div>