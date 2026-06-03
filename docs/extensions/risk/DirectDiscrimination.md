---
search:
  boost: 10.0
---

# Class: DirectDiscrimination 


_Occurs when a person is treated less favourably than another in a_

_comparable situation based on a protected characteristic (e.g., race,_

_sex, disability)_



<div data-search-exclude markdown="1">



URI: [risk:DirectDiscrimination](https://w3id.org/lmodel/dpv/risk/DirectDiscrimination)





```mermaid
 classDiagram
    class DirectDiscrimination
    click DirectDiscrimination href "../DirectDiscrimination/"
      PotentialConsequence <|-- DirectDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- DirectDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- DirectDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- DirectDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **DirectDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DirectDiscrimination](https://w3id.org/lmodel/dpv/risk/DirectDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Direct Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DirectDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DirectDiscrimination |
| native | risk:DirectDiscrimination |
| exact | dpv_risk:DirectDiscrimination, dpv_risk_owl:DirectDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DirectDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DirectDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Occurs when a person is treated less favourably than another in a

  comparable situation based on a protected characteristic (e.g., race,

  sex, disability)'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Direct Discrimination
exact_mappings:
- dpv_risk:DirectDiscrimination
- dpv_risk_owl:DirectDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:DirectDiscrimination

```
</details>

### Induced

<details>
```yaml
name: DirectDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DirectDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Occurs when a person is treated less favourably than another in a

  comparable situation based on a protected characteristic (e.g., race,

  sex, disability)'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Direct Discrimination
exact_mappings:
- dpv_risk:DirectDiscrimination
- dpv_risk_owl:DirectDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:DirectDiscrimination

```
</details></div>