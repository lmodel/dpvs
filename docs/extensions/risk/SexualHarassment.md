---
search:
  boost: 10.0
---

# Class: SexualHarassment 


_Concept representing sexual harassment of individual(s)_



<div data-search-exclude markdown="1">



URI: [risk:SexualHarassment](https://w3id.org/lmodel/dpv/risk/SexualHarassment)





```mermaid
 classDiagram
    class SexualHarassment
    click SexualHarassment href "../SexualHarassment/"
      PotentialConsequence <|-- SexualHarassment
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- SexualHarassment
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- SexualHarassment
        click PotentialRisk href "../PotentialRisk/"
      Harassment <|-- SexualHarassment
        click Harassment href "../Harassment/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Harm](Harm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
                * [Harassment](Harassment.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [Wellbeing](Wellbeing.md)]
                    * **SexualHarassment** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SexualHarassment](https://w3id.org/lmodel/dpv/risk/SexualHarassment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Sexual Harassment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SexualHarassment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SexualHarassment |
| native | risk:SexualHarassment |
| exact | dpv_risk:SexualHarassment, dpv_risk_owl:SexualHarassment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SexualHarassment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SexualHarassment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing sexual harassment of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sexual Harassment
exact_mappings:
- dpv_risk:SexualHarassment
- dpv_risk_owl:SexualHarassment
is_a: Harassment
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SexualHarassment

```
</details>

### Induced

<details>
```yaml
name: SexualHarassment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SexualHarassment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing sexual harassment of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Sexual Harassment
exact_mappings:
- dpv_risk:SexualHarassment
- dpv_risk_owl:SexualHarassment
is_a: Harassment
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:SexualHarassment

```
</details></div>