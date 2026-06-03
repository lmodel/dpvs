---
search:
  boost: 10.0
---

# Class: RacialDiscrimination 


_Discrimination against individuals because of their racial background or_

_skin colour_



<div data-search-exclude markdown="1">



URI: [risk:RacialDiscrimination](https://w3id.org/lmodel/dpv/risk/RacialDiscrimination)





```mermaid
 classDiagram
    class RacialDiscrimination
    click RacialDiscrimination href "../RacialDiscrimination/"
      PotentialConsequence <|-- RacialDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- RacialDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- RacialDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Racism <|-- RacialDiscrimination
        click Racism href "../Racism/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Racism](Racism.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **RacialDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RacialDiscrimination](https://w3id.org/lmodel/dpv/risk/RacialDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Racial Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RacialDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RacialDiscrimination |
| native | risk:RacialDiscrimination |
| exact | dpv_risk:RacialDiscrimination, dpv_risk_owl:RacialDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RacialDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RacialDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination against individuals because of their racial background
  or

  skin colour'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Racial Discrimination
exact_mappings:
- dpv_risk:RacialDiscrimination
- dpv_risk_owl:RacialDiscrimination
is_a: Racism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:RacialDiscrimination

```
</details>

### Induced

<details>
```yaml
name: RacialDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RacialDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination against individuals because of their racial background
  or

  skin colour'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Racial Discrimination
exact_mappings:
- dpv_risk:RacialDiscrimination
- dpv_risk_owl:RacialDiscrimination
is_a: Racism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:RacialDiscrimination

```
</details></div>