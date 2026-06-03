---
search:
  boost: 5.0
---

# Slot: controls 


_Indicates this control manages specified risk concept event or action,_

_such as for risk sources, risks, consequences, and impacts_



<div data-search-exclude markdown="1">



URI: [risk:controls](https://w3id.org/lmodel/dpv/risk/controls)

## Inheritance

* **controls**
    * [contains](contains.md)
    * [investigates](investigates.md)
    * [monitors](monitors.md)
    * [overrides](overrides.md)
    * [reduces](reduces.md)
    * [resolves](resolves.md)
    * [shares](shares.md)
    * [transfers](transfers.md)








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


* control




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#controls |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:controls |
| native | risk:controls |
| exact | dpv_risk:controls, dpv_risk_owl:controls |




## LinkML Source

<details>
```yaml
name: controls
definition_uri: risk:controls
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#controls
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates this control manages specified risk concept event or action,

  such as for risk sources, risks, consequences, and impacts'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- control
exact_mappings:
- dpv_risk:controls
- dpv_risk_owl:controls
rank: 1000
range: string
multivalued: true

```
</details></div>