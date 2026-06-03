---
search:
  boost: 5.0
---

# Slot: has_auditor 


_Indicates technology auditor_



<div data-search-exclude markdown="1">



URI: [tech:has_auditor](https://w3id.org/lmodel/dpv/tech/has_auditor)

## Inheritance

* [has_actor](has_actor.md)
    * **has_auditor**








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


* has auditor




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasAuditor |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_auditor |
| native | tech:has_auditor |
| exact | dpv_tech:hasAuditor, dpv_tech_owl:hasAuditor |




## LinkML Source

<details>
```yaml
name: has_auditor
definition_uri: tech:hasAuditor
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasAuditor
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology auditor
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has auditor
exact_mappings:
- dpv_tech:hasAuditor
- dpv_tech_owl:hasAuditor
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>