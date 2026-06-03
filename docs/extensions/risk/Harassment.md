---
search:
  boost: 10.0
---

# Class: Harassment 


_Concept representing harassment of individual(s)_



<div data-search-exclude markdown="1">



URI: [risk:Harassment](https://w3id.org/lmodel/dpv/risk/Harassment)





```mermaid
 classDiagram
    class Harassment
    click Harassment href "../Harassment/"
      PotentialConsequence <|-- Harassment
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Harassment
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Harassment
        click PotentialRisk href "../PotentialRisk/"
      Wellbeing <|-- Harassment
        click Wellbeing href "../Wellbeing/"
      Harm <|-- Harassment
        click Harm href "../Harm/"
      

      Harassment <|-- SexualHarassment
        click SexualHarassment href "../SexualHarassment/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Harm](Harm.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]
                * **Harassment** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [Wellbeing](Wellbeing.md)]
                    * [SexualHarassment](SexualHarassment.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Harassment](https://w3id.org/lmodel/dpv/risk/Harassment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Harassment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Harassment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Harassment |
| native | risk:Harassment |
| exact | dpv_risk:Harassment, dpv_risk_owl:Harassment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Harassment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Harassment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing harassment of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Harassment
exact_mappings:
- dpv_risk:Harassment
- dpv_risk_owl:Harassment
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- Wellbeing
class_uri: risk:Harassment

```
</details>

### Induced

<details>
```yaml
name: Harassment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Harassment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing harassment of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Harassment
exact_mappings:
- dpv_risk:Harassment
- dpv_risk_owl:Harassment
is_a: Harm
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- Wellbeing
class_uri: risk:Harassment

```
</details></div>