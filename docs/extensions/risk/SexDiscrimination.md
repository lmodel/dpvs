---
search:
  boost: 10.0
---

# Class: SexDiscrimination 


_Discrimination based on a person's biological sex_



<div data-search-exclude markdown="1">



URI: [risk:SexDiscrimination](https://w3id.org/lmodel/dpv/risk/SexDiscrimination)





```mermaid
 classDiagram
    class SexDiscrimination
    click SexDiscrimination href "../SexDiscrimination/"
      PotentialConsequence <|-- SexDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- SexDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- SexDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Sexism <|-- SexDiscrimination
        click Sexism href "../Sexism/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Sexism](Sexism.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **SexDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SexDiscrimination](https://w3id.org/lmodel/dpv/risk/SexDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Sex Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SexDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SexDiscrimination |
| native | risk:SexDiscrimination |
| exact | dpv_risk:SexDiscrimination, dpv_risk_owl:SexDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SexDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SexDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's biological sex
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sex Discrimination
exact_mappings:
- dpv_risk:SexDiscrimination
- dpv_risk_owl:SexDiscrimination
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SexDiscrimination

```
</details>

### Induced

<details>
```yaml
name: SexDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SexDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Discrimination based on a person's biological sex
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sex Discrimination
exact_mappings:
- dpv_risk:SexDiscrimination
- dpv_risk_owl:SexDiscrimination
is_a: Sexism
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SexDiscrimination

```
</details></div>