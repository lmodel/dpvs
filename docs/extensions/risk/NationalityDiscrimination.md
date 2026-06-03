---
search:
  boost: 10.0
---

# Class: NationalityDiscrimination 


_Discrimination based on a person's nationality or citizenship_



<div data-search-exclude markdown="1">



URI: [risk:NationalityDiscrimination](https://w3id.org/lmodel/dpv/risk/NationalityDiscrimination)





```mermaid
 classDiagram
    class NationalityDiscrimination
    click NationalityDiscrimination href "../NationalityDiscrimination/"
      PotentialConsequence <|-- NationalityDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- NationalityDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- NationalityDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- NationalityDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **NationalityDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:NationalityDiscrimination](https://w3id.org/lmodel/dpv/risk/NationalityDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Nationality Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#NationalityDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:NationalityDiscrimination |
| native | risk:NationalityDiscrimination |
| exact | dpv_risk:NationalityDiscrimination, dpv_risk_owl:NationalityDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NationalityDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#NationalityDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's nationality or citizenship
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Nationality Discrimination
exact_mappings:
- dpv_risk:NationalityDiscrimination
- dpv_risk_owl:NationalityDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:NationalityDiscrimination

```
</details>

### Induced

<details>
```yaml
name: NationalityDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#NationalityDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's nationality or citizenship
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Nationality Discrimination
exact_mappings:
- dpv_risk:NationalityDiscrimination
- dpv_risk_owl:NationalityDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:NationalityDiscrimination

```
</details></div>