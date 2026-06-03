---
search:
  boost: 10.0
---

# Class: Homophobia 


_Hostility or prejudice against individuals who are or are perceived to_

_be homosexual_



<div data-search-exclude markdown="1">



URI: [risk:Homophobia](https://w3id.org/lmodel/dpv/risk/Homophobia)





```mermaid
 classDiagram
    class Homophobia
    click Homophobia href "../Homophobia/"
      PotentialConsequence <|-- Homophobia
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Homophobia
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Homophobia
        click PotentialRisk href "../PotentialRisk/"
      SexualOrientationDiscrimination <|-- Homophobia
        click SexualOrientationDiscrimination href "../SexualOrientationDiscrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [SexualOrientationDiscrimination](SexualOrientationDiscrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Homophobia** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Homophobia](https://w3id.org/lmodel/dpv/risk/Homophobia) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Homophobia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Homophobia |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Homophobia |
| native | risk:Homophobia |
| exact | dpv_risk:Homophobia, dpv_risk_owl:Homophobia |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Homophobia
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Homophobia
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Hostility or prejudice against individuals who are or are perceived
  to

  be homosexual'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Homophobia
exact_mappings:
- dpv_risk:Homophobia
- dpv_risk_owl:Homophobia
is_a: SexualOrientationDiscrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Homophobia

```
</details>

### Induced

<details>
```yaml
name: Homophobia
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Homophobia
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Hostility or prejudice against individuals who are or are perceived
  to

  be homosexual'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Homophobia
exact_mappings:
- dpv_risk:Homophobia
- dpv_risk_owl:Homophobia
is_a: SexualOrientationDiscrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Homophobia

```
</details></div>