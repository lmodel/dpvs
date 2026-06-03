---
search:
  boost: 10.0
---

# Class: GenderDiscrimination 


_Discrimination based on a person's gender identity or gender expression_



<div data-search-exclude markdown="1">



URI: [risk:GenderDiscrimination](https://w3id.org/lmodel/dpv/risk/GenderDiscrimination)





```mermaid
 classDiagram
    class GenderDiscrimination
    click GenderDiscrimination href "../GenderDiscrimination/"
      PotentialConsequence <|-- GenderDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- GenderDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- GenderDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Sexism <|-- GenderDiscrimination
        click Sexism href "../Sexism/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Sexism](Sexism.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **GenderDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:GenderDiscrimination](https://w3id.org/lmodel/dpv/risk/GenderDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Gender Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#GenderDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:GenderDiscrimination |
| native | risk:GenderDiscrimination |
| exact | dpv_risk:GenderDiscrimination, dpv_risk_owl:GenderDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GenderDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GenderDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's gender identity or gender expression
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Gender Discrimination
exact_mappings:
- dpv_risk:GenderDiscrimination
- dpv_risk_owl:GenderDiscrimination
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:GenderDiscrimination

```
</details>

### Induced

<details>
```yaml
name: GenderDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GenderDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's gender identity or gender expression
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Gender Discrimination
exact_mappings:
- dpv_risk:GenderDiscrimination
- dpv_risk_owl:GenderDiscrimination
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:GenderDiscrimination

```
</details></div>