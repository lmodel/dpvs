---
search:
  boost: 10.0
---

# Class: SexualOrientationDiscrimination 


_Discrimination based on a person's sexual orientation, typically against_

_those who are not heterosexual_



<div data-search-exclude markdown="1">



URI: [risk:SexualOrientationDiscrimination](https://w3id.org/lmodel/dpv/risk/SexualOrientationDiscrimination)





```mermaid
 classDiagram
    class SexualOrientationDiscrimination
    click SexualOrientationDiscrimination href "../SexualOrientationDiscrimination/"
      PotentialConsequence <|-- SexualOrientationDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- SexualOrientationDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- SexualOrientationDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- SexualOrientationDiscrimination
        click Discrimination href "../Discrimination/"
      

      SexualOrientationDiscrimination <|-- Homophobia
        click Homophobia href "../Homophobia/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **SexualOrientationDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Homophobia](Homophobia.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SexualOrientationDiscrimination](https://w3id.org/lmodel/dpv/risk/SexualOrientationDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* SexualOrientation Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SexualOrientationDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SexualOrientationDiscrimination |
| native | risk:SexualOrientationDiscrimination |
| exact | dpv_risk:SexualOrientationDiscrimination, dpv_risk_owl:SexualOrientationDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SexualOrientationDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SexualOrientationDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s sexual orientation, typically against

  those who are not heterosexual'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- SexualOrientation Discrimination
exact_mappings:
- dpv_risk:SexualOrientationDiscrimination
- dpv_risk_owl:SexualOrientationDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SexualOrientationDiscrimination

```
</details>

### Induced

<details>
```yaml
name: SexualOrientationDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SexualOrientationDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s sexual orientation, typically against

  those who are not heterosexual'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- SexualOrientation Discrimination
exact_mappings:
- dpv_risk:SexualOrientationDiscrimination
- dpv_risk_owl:SexualOrientationDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SexualOrientationDiscrimination

```
</details></div>