---
search:
  boost: 5.0
---

# Slot: has_risk_source 


_Indicates the risk (subject) has the indicated risk source (object)_



<div data-search-exclude markdown="1">



URI: [risk:has_risk_source](https://w3id.org/lmodel/dpv/risk/has_risk_source)
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


* has risk source




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasRiskSource |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_risk_source |
| native | risk:has_risk_source |
| exact | dpv_risk:hasRiskSource, dpv_risk_owl:hasRiskSource |




## LinkML Source

<details>
```yaml
name: has_risk_source
definition_uri: risk:hasRiskSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasRiskSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the risk (subject) has the indicated risk source (object)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has risk source
exact_mappings:
- dpv_risk:hasRiskSource
- dpv_risk_owl:hasRiskSource
rank: 1000
range: string
multivalued: true

```
</details></div>