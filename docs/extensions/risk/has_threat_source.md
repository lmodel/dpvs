---
search:
  boost: 5.0
---

# Slot: has_threat_source 


_Indicates the threat (subject) has the indicated source (object)_



<div data-search-exclude markdown="1">



URI: [risk:has_threat_source](https://w3id.org/lmodel/dpv/risk/has_threat_source)
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


* has threat source




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasThreatSource |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_threat_source |
| native | risk:has_threat_source |
| exact | dpv_risk:hasThreatSource, dpv_risk_owl:hasThreatSource |




## LinkML Source

<details>
```yaml
name: has_threat_source
definition_uri: risk:hasThreatSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasThreatSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates the threat (subject) has the indicated source (object)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has threat source
exact_mappings:
- dpv_risk:hasThreatSource
- dpv_risk_owl:hasThreatSource
rank: 1000
range: string
multivalued: true

```
</details></div>