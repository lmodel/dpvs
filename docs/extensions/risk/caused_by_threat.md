---
search:
  boost: 5.0
---

# Slot: caused_by_threat 


_Indicates the cause of associated context (subject) was the indicated_

_threat (object)_



<div data-search-exclude markdown="1">



URI: [risk:caused_by_threat](https://w3id.org/lmodel/dpv/risk/caused_by_threat)
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


* caused by threat




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#causedByThreat |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:caused_by_threat |
| native | risk:caused_by_threat |
| exact | dpv_risk:causedByThreat, dpv_risk_owl:causedByThreat |




## LinkML Source

<details>
```yaml
name: caused_by_threat
definition_uri: risk:causedByThreat
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#causedByThreat
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates the cause of associated context (subject) was the indicated

  threat (object)'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- caused by threat
exact_mappings:
- dpv_risk:causedByThreat
- dpv_risk_owl:causedByThreat
rank: 1000
range: string
multivalued: true

```
</details></div>