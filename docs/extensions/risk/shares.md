---
search:
  boost: 5.0
---

# Slot: shares 


_Indicates the specified event or action is shared with another context_

_or entity by this control_



<div data-search-exclude markdown="1">



URI: [risk:shares](https://w3id.org/lmodel/dpv/risk/shares)

## Inheritance

* [controls](controls.md)
    * **shares**








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


* shares




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#shares |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:shares |
| native | risk:shares |
| exact | dpv_risk:shares, dpv_risk_owl:shares |




## LinkML Source

<details>
```yaml
name: shares
definition_uri: risk:shares
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#shares
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates the specified event or action is shared with another context

  or entity by this control'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- shares
exact_mappings:
- dpv_risk:shares
- dpv_risk_owl:shares
rank: 1000
is_a: controls
range: string
multivalued: true

```
</details></div>