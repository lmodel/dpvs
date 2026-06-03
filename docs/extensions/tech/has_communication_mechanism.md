---
search:
  boost: 5.0
---

# Slot: has_communication_mechanism 


_Indicates communication mechanisms used or provided by technology_



<div data-search-exclude markdown="1">



URI: [tech:has_communication_mechanism](https://w3id.org/lmodel/dpv/tech/has_communication_mechanism)
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


* has communication mechanism




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasCommunicationMechanism |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_communication_mechanism |
| native | tech:has_communication_mechanism |
| exact | dpv_tech:hasCommunicationMechanism, dpv_tech_owl:hasCommunicationMechanism |




## LinkML Source

<details>
```yaml
name: has_communication_mechanism
definition_uri: tech:hasCommunicationMechanism
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasCommunicationMechanism
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates communication mechanisms used or provided by technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has communication mechanism
exact_mappings:
- dpv_tech:hasCommunicationMechanism
- dpv_tech_owl:hasCommunicationMechanism
rank: 1000
range: string
multivalued: true

```
</details></div>