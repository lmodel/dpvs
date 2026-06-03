---
search:
  boost: 5.0
---

# Slot: refers_to_risk 


_Indicates the incident (subject) is a materialisation of the indicated_

_risk (object)_



<div data-search-exclude markdown="1">



URI: [risk:refers_to_risk](https://w3id.org/lmodel/dpv/risk/refers_to_risk)
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


* [RiskSubset](RiskSubset.md)



## Aliases


* refers to risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#refersToRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:refers_to_risk |
| native | risk:refers_to_risk |
| exact | dpv_risk:refersToRisk, dpv_risk_owl:refersToRisk |




## LinkML Source

<details>
```yaml
name: refers_to_risk
definition_uri: risk:refersToRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#refersToRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates the incident (subject) is a materialisation of the indicated

  risk (object)'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- refers to risk
exact_mappings:
- dpv_risk:refersToRisk
- dpv_risk_owl:refersToRisk
rank: 1000
range: string
multivalued: true

```
</details></div>