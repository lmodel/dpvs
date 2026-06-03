---
search:
  boost: 5.0
---

# Slot: has_subject 


_Indicates technology subject_



<div data-search-exclude markdown="1">



URI: [tech:has_subject](https://w3id.org/lmodel/dpv/tech/has_subject)

## Inheritance

* [has_actor](has_actor.md)
    * **has_subject**








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


* has subject




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasSubject |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_subject |
| native | tech:has_subject |
| exact | dpv_tech:hasSubject, dpv_tech_owl:hasSubject |




## LinkML Source

<details>
```yaml
name: has_subject
definition_uri: tech:hasSubject
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasSubject
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology subject
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has subject
exact_mappings:
- dpv_tech:hasSubject
- dpv_tech_owl:hasSubject
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>