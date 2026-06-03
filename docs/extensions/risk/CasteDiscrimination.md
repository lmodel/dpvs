---
search:
  boost: 10.0
---

# Class: CasteDiscrimination 


_Discrimination based on a person's caste, a form of social_

_stratification found in some cultures_



<div data-search-exclude markdown="1">



URI: [risk:CasteDiscrimination](https://w3id.org/lmodel/dpv/risk/CasteDiscrimination)





```mermaid
 classDiagram
    class CasteDiscrimination
    click CasteDiscrimination href "../CasteDiscrimination/"
      PotentialConsequence <|-- CasteDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- CasteDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- CasteDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- CasteDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **CasteDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CasteDiscrimination](https://w3id.org/lmodel/dpv/risk/CasteDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Caste Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#CasteDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CasteDiscrimination |
| native | risk:CasteDiscrimination |
| exact | dpv_risk:CasteDiscrimination, dpv_risk_owl:CasteDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CasteDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CasteDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s caste, a form of social

  stratification found in some cultures'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Caste Discrimination
exact_mappings:
- dpv_risk:CasteDiscrimination
- dpv_risk_owl:CasteDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:CasteDiscrimination

```
</details>

### Induced

<details>
```yaml
name: CasteDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CasteDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s caste, a form of social

  stratification found in some cultures'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Caste Discrimination
exact_mappings:
- dpv_risk:CasteDiscrimination
- dpv_risk_owl:CasteDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:CasteDiscrimination

```
</details></div>