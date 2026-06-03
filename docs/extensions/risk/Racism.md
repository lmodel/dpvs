---
search:
  boost: 10.0
---

# Class: Racism 


_Prejudice or discrimination against people based on their race_



<div data-search-exclude markdown="1">



URI: [risk:Racism](https://w3id.org/lmodel/dpv/risk/Racism)





```mermaid
 classDiagram
    class Racism
    click Racism href "../Racism/"
      PotentialConsequence <|-- Racism
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Racism
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Racism
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- Racism
        click Discrimination href "../Discrimination/"
      

      Racism <|-- EthnicDiscrimination
        click EthnicDiscrimination href "../EthnicDiscrimination/"
      Racism <|-- RacialDiscrimination
        click RacialDiscrimination href "../RacialDiscrimination/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **Racism** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [EthnicDiscrimination](EthnicDiscrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [RacialDiscrimination](RacialDiscrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Racism](https://w3id.org/lmodel/dpv/risk/Racism) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Racism




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Racism |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Racism |
| native | risk:Racism |
| exact | dpv_risk:Racism, dpv_risk_owl:Racism |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Racism
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Racism
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Prejudice or discrimination against people based on their race
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Racism
exact_mappings:
- dpv_risk:Racism
- dpv_risk_owl:Racism
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Racism

```
</details>

### Induced

<details>
```yaml
name: Racism
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Racism
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Prejudice or discrimination against people based on their race
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Racism
exact_mappings:
- dpv_risk:Racism
- dpv_risk_owl:Racism
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Racism

```
</details></div>