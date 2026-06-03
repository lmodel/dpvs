---
search:
  boost: 10.0
---

# Class: UnfavourableTreatment 


_A treatment is unfavourable when the person(s) is treated poorly or less_

_favorably due to specific reasons compared to other person(s)_



<div data-search-exclude markdown="1">



URI: [risk:UnfavourableTreatment](https://w3id.org/lmodel/dpv/risk/UnfavourableTreatment)





```mermaid
 classDiagram
    class UnfavourableTreatment
    click UnfavourableTreatment href "../UnfavourableTreatment/"
      PotentialConsequence <|-- UnfavourableTreatment
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- UnfavourableTreatment
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- UnfavourableTreatment
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- UnfavourableTreatment
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **UnfavourableTreatment** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnfavourableTreatment](https://w3id.org/lmodel/dpv/risk/UnfavourableTreatment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unfavoural Treatment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnfavourableTreatment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnfavourableTreatment |
| native | risk:UnfavourableTreatment |
| exact | dpv_risk:UnfavourableTreatment, dpv_risk_owl:UnfavourableTreatment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnfavourableTreatment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnfavourableTreatment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A treatment is unfavourable when the person(s) is treated poorly or
  less

  favorably due to specific reasons compared to other person(s)'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unfavoural Treatment
exact_mappings:
- dpv_risk:UnfavourableTreatment
- dpv_risk_owl:UnfavourableTreatment
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:UnfavourableTreatment

```
</details>

### Induced

<details>
```yaml
name: UnfavourableTreatment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnfavourableTreatment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'A treatment is unfavourable when the person(s) is treated poorly or
  less

  favorably due to specific reasons compared to other person(s)'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unfavoural Treatment
exact_mappings:
- dpv_risk:UnfavourableTreatment
- dpv_risk_owl:UnfavourableTreatment
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:UnfavourableTreatment

```
</details></div>