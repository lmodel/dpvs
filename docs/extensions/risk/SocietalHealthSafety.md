---
search:
  boost: 10.0
---

# Class: SocietalHealthSafety 


_Concept representing health and safety of society at large_



<div data-search-exclude markdown="1">



URI: [risk:SocietalHealthSafety](https://w3id.org/lmodel/dpv/risk/SocietalHealthSafety)





```mermaid
 classDiagram
    class SocietalHealthSafety
    click SocietalHealthSafety href "../SocietalHealthSafety/"
      PotentialConsequence <|-- SocietalHealthSafety
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- SocietalHealthSafety
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- SocietalHealthSafety
        click PotentialRisk href "../PotentialRisk/"
      GroupRisk <|-- SocietalHealthSafety
        click GroupRisk href "../GroupRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [GroupRisk](GroupRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **SocietalHealthSafety** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SocietalHealthSafety](https://w3id.org/lmodel/dpv/risk/SocietalHealthSafety) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Societal Health & Safety




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SocietalHealthSafety |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SocietalHealthSafety |
| native | risk:SocietalHealthSafety |
| exact | dpv_risk:SocietalHealthSafety, dpv_risk_owl:SocietalHealthSafety |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SocietalHealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SocietalHealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing health and safety of society at large
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Societal Health & Safety
exact_mappings:
- dpv_risk:SocietalHealthSafety
- dpv_risk_owl:SocietalHealthSafety
is_a: GroupRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SocietalHealthSafety

```
</details>

### Induced

<details>
```yaml
name: SocietalHealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SocietalHealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing health and safety of society at large
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Societal Health & Safety
exact_mappings:
- dpv_risk:SocietalHealthSafety
- dpv_risk_owl:SocietalHealthSafety
is_a: GroupRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SocietalHealthSafety

```
</details></div>