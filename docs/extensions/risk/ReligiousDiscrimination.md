---
search:
  boost: 10.0
---

# Class: ReligiousDiscrimination 


_Discrimination based on a person's religion or religious beliefs or_

_practices_



<div data-search-exclude markdown="1">



URI: [risk:ReligiousDiscrimination](https://w3id.org/lmodel/dpv/risk/ReligiousDiscrimination)





```mermaid
 classDiagram
    class ReligiousDiscrimination
    click ReligiousDiscrimination href "../ReligiousDiscrimination/"
      PotentialConsequence <|-- ReligiousDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ReligiousDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ReligiousDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- ReligiousDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ReligiousDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ReligiousDiscrimination](https://w3id.org/lmodel/dpv/risk/ReligiousDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Religious Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ReligiousDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ReligiousDiscrimination |
| native | risk:ReligiousDiscrimination |
| exact | dpv_risk:ReligiousDiscrimination, dpv_risk_owl:ReligiousDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReligiousDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReligiousDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s religion or religious beliefs or

  practices'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Religious Discrimination
exact_mappings:
- dpv_risk:ReligiousDiscrimination
- dpv_risk_owl:ReligiousDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ReligiousDiscrimination

```
</details>

### Induced

<details>
```yaml
name: ReligiousDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReligiousDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination based on a person''s religion or religious beliefs or

  practices'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Religious Discrimination
exact_mappings:
- dpv_risk:ReligiousDiscrimination
- dpv_risk_owl:ReligiousDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ReligiousDiscrimination

```
</details></div>