---
search:
  boost: 5.0
---

# Slot: has_partner 


_Indicates technology partner_



<div data-search-exclude markdown="1">



URI: [tech:has_partner](https://w3id.org/lmodel/dpv/tech/has_partner)

## Inheritance

* [has_actor](has_actor.md)
    * **has_partner**








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


* has partner




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasPartner |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_partner |
| native | tech:has_partner |
| exact | dpv_tech:hasPartner, dpv_tech_owl:hasPartner |




## LinkML Source

<details>
```yaml
name: has_partner
definition_uri: tech:hasPartner
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasPartner
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates technology partner
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has partner
exact_mappings:
- dpv_tech:hasPartner
- dpv_tech_owl:hasPartner
rank: 1000
is_a: has_actor
range: string
multivalued: true

```
</details></div>