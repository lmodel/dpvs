---
search:
  boost: 10.0
---

# Class: ThreatSource 


_Source of threat event, including both agent and non-agent sources_



<div data-search-exclude markdown="1">



URI: [risk:ThreatSource](https://w3id.org/lmodel/dpv/risk/ThreatSource)





```mermaid
 classDiagram
    class ThreatSource
    click ThreatSource href "../ThreatSource/"
      RiskIdentification <|-- ThreatSource
        click RiskIdentification href "../RiskIdentification/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * [RiskIdentification](RiskIdentification.md)
            * **ThreatSource**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ThreatSource](https://w3id.org/lmodel/dpv/risk/ThreatSource) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Threat Source




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ThreatSource |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ThreatSource |
| native | risk:ThreatSource |
| exact | dpv_risk:ThreatSource, dpv_risk_owl:ThreatSource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ThreatSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ThreatSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Source of threat event, including both agent and non-agent sources
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Threat Source
exact_mappings:
- dpv_risk:ThreatSource
- dpv_risk_owl:ThreatSource
is_a: RiskIdentification
class_uri: risk:ThreatSource

```
</details>

### Induced

<details>
```yaml
name: ThreatSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ThreatSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Source of threat event, including both agent and non-agent sources
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Threat Source
exact_mappings:
- dpv_risk:ThreatSource
- dpv_risk_owl:ThreatSource
is_a: RiskIdentification
class_uri: risk:ThreatSource

```
</details></div>