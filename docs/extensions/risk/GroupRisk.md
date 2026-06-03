---
search:
  boost: 10.0
---

# Class: GroupRisk 


_Risks and issues that affect or have the potential to affect groups in_

_society_



<div data-search-exclude markdown="1">



URI: [risk:GroupRisk](https://w3id.org/lmodel/dpv/risk/GroupRisk)





```mermaid
 classDiagram
    class GroupRisk
    click GroupRisk href "../GroupRisk/"
      PotentialConsequence <|-- GroupRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- GroupRisk
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- GroupRisk
        click PotentialRisk href "../PotentialRisk/"
      SocietalRiskConcept <|-- GroupRisk
        click SocietalRiskConcept href "../SocietalRiskConcept/"
      

      GroupRisk <|-- GroupHealthSafety
        click GroupHealthSafety href "../GroupHealthSafety/"
      GroupRisk <|-- SocialDisadvantage
        click SocialDisadvantage href "../SocialDisadvantage/"
      GroupRisk <|-- SocietalHealthSafety
        click SocietalHealthSafety href "../SocietalHealthSafety/"
      GroupRisk <|-- Terrorism
        click Terrorism href "../Terrorism/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **GroupRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [GroupHealthSafety](GroupHealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [HealthSafety](HealthSafety.md)]
        * [SocialDisadvantage](SocialDisadvantage.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [SocietalHealthSafety](SocietalHealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Terrorism](Terrorism.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:GroupRisk](https://w3id.org/lmodel/dpv/risk/GroupRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Societal Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#GroupRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:GroupRisk |
| native | risk:GroupRisk |
| exact | dpv_risk:GroupRisk, dpv_risk_owl:GroupRisk |
| related | iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GroupRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GroupRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risks and issues that affect or have the potential to affect groups
  in

  society'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Societal Risk
exact_mappings:
- dpv_risk:GroupRisk
- dpv_risk_owl:GroupRisk
related_mappings:
- iso42001:AIRisk
is_a: SocietalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:GroupRisk

```
</details>

### Induced

<details>
```yaml
name: GroupRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GroupRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risks and issues that affect or have the potential to affect groups
  in

  society'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Societal Risk
exact_mappings:
- dpv_risk:GroupRisk
- dpv_risk_owl:GroupRisk
related_mappings:
- iso42001:AIRisk
is_a: SocietalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:GroupRisk

```
</details></div>