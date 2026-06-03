---
search:
  boost: 10.0
---

# Class: SocialDisadvantage 


_Concept representing Social Disadvantage_



<div data-search-exclude markdown="1">



URI: [risk:SocialDisadvantage](https://w3id.org/lmodel/dpv/risk/SocialDisadvantage)





```mermaid
 classDiagram
    class SocialDisadvantage
    click SocialDisadvantage href "../SocialDisadvantage/"
      PotentialConsequence <|-- SocialDisadvantage
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- SocialDisadvantage
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- SocialDisadvantage
        click PotentialRisk href "../PotentialRisk/"
      GroupRisk <|-- SocialDisadvantage
        click GroupRisk href "../GroupRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [GroupRisk](GroupRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **SocialDisadvantage** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SocialDisadvantage](https://w3id.org/lmodel/dpv/risk/SocialDisadvantage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Social Disadvantage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SocialDisadvantage |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SocialDisadvantage |
| native | risk:SocialDisadvantage |
| exact | dpv_risk:SocialDisadvantage, dpv_risk_owl:SocialDisadvantage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SocialDisadvantage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SocialDisadvantage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Social Disadvantage
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Social Disadvantage
exact_mappings:
- dpv_risk:SocialDisadvantage
- dpv_risk_owl:SocialDisadvantage
is_a: GroupRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SocialDisadvantage

```
</details>

### Induced

<details>
```yaml
name: SocialDisadvantage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SocialDisadvantage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Social Disadvantage
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Social Disadvantage
exact_mappings:
- dpv_risk:SocialDisadvantage
- dpv_risk_owl:SocialDisadvantage
is_a: GroupRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SocialDisadvantage

```
</details></div>