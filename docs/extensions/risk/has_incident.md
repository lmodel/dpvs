---
search:
  boost: 5.0
---

# Slot: has_incident 


_Indicates an incident is associated with the specified context_



<div data-search-exclude markdown="1">



URI: [risk:has_incident](https://w3id.org/lmodel/dpv/risk/has_incident)
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


* has incident




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#hasIncident |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:has_incident |
| native | risk:has_incident |
| exact | dpv_risk:hasIncident, dpv_risk_owl:hasIncident |




## LinkML Source

<details>
```yaml
name: has_incident
definition_uri: risk:hasIncident
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#hasIncident
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Indicates an incident is associated with the specified context
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- has incident
exact_mappings:
- dpv_risk:hasIncident
- dpv_risk_owl:hasIncident
rank: 1000
range: string
multivalued: true

```
</details></div>