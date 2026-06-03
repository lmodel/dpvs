---
search:
  boost: 10.0
---

# Class: ReverseDiscrimination 


_Discrimination against members of a majority or historically dominant_

_group, often in the context of efforts to promote equality_



<div data-search-exclude markdown="1">



URI: [risk:ReverseDiscrimination](https://w3id.org/lmodel/dpv/risk/ReverseDiscrimination)





```mermaid
 classDiagram
    class ReverseDiscrimination
    click ReverseDiscrimination href "../ReverseDiscrimination/"
      PotentialConsequence <|-- ReverseDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ReverseDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ReverseDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- ReverseDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ReverseDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ReverseDiscrimination](https://w3id.org/lmodel/dpv/risk/ReverseDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Reverse Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ReverseDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ReverseDiscrimination |
| native | risk:ReverseDiscrimination |
| exact | dpv_risk:ReverseDiscrimination, dpv_risk_owl:ReverseDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReverseDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReverseDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination against members of a majority or historically dominant

  group, often in the context of efforts to promote equality'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reverse Discrimination
exact_mappings:
- dpv_risk:ReverseDiscrimination
- dpv_risk_owl:ReverseDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ReverseDiscrimination

```
</details>

### Induced

<details>
```yaml
name: ReverseDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReverseDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination against members of a majority or historically dominant

  group, often in the context of efforts to promote equality'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reverse Discrimination
exact_mappings:
- dpv_risk:ReverseDiscrimination
- dpv_risk_owl:ReverseDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ReverseDiscrimination

```
</details></div>