---
search:
  boost: 5.0
---

# Slot: transfers 


_Indicates the specified event or action is transferred to another_

_context or entity by this control_



<div data-search-exclude markdown="1">



URI: [risk:transfers](https://w3id.org/lmodel/dpv/risk/transfers)

## Inheritance

* [controls](controls.md)
    * **transfers**








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


* [RiskSubset](RiskSubset.md)



## Aliases


* transfers




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#transfers |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:transfers |
| native | risk:transfers |
| exact | dpv_risk:transfers, dpv_risk_owl:transfers |




## LinkML Source

<details>
```yaml
name: transfers
definition_uri: risk:transfers
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#transfers
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates the specified event or action is transferred to another

  context or entity by this control'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- transfers
exact_mappings:
- dpv_risk:transfers
- dpv_risk_owl:transfers
rank: 1000
is_a: controls
range: string
multivalued: true

```
</details></div>