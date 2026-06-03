---
search:
  boost: 10.0
---

# Class: LanguageDiscrimination 


_Discrimination based on a person's language, often linked to national_

_origin or ethnicity_



<div data-search-exclude markdown="1">



URI: [risk:LanguageDiscrimination](https://w3id.org/lmodel/dpv/risk/LanguageDiscrimination)





```mermaid
 classDiagram
    class LanguageDiscrimination
    click LanguageDiscrimination href "../LanguageDiscrimination/"
      PotentialConsequence <|-- LanguageDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- LanguageDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- LanguageDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- LanguageDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **LanguageDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:LanguageDiscrimination](https://w3id.org/lmodel/dpv/risk/LanguageDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Language Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#LanguageDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:LanguageDiscrimination |
| native | risk:LanguageDiscrimination |
| exact | dpv_risk:LanguageDiscrimination, dpv_risk_owl:LanguageDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LanguageDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LanguageDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s language, often linked to national

  origin or ethnicity'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Language Discrimination
exact_mappings:
- dpv_risk:LanguageDiscrimination
- dpv_risk_owl:LanguageDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:LanguageDiscrimination

```
</details>

### Induced

<details>
```yaml
name: LanguageDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LanguageDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s language, often linked to national

  origin or ethnicity'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Language Discrimination
exact_mappings:
- dpv_risk:LanguageDiscrimination
- dpv_risk_owl:LanguageDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:LanguageDiscrimination

```
</details></div>