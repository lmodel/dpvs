---
search:
  boost: 10.0
---

# Class: Benefit 


_Concept representing benefits - both material and immaterial_



<div data-search-exclude markdown="1">



URI: [risk:Benefit](https://w3id.org/lmodel/dpv/risk/Benefit)





```mermaid
 classDiagram
    class Benefit
    click Benefit href "../Benefit/"
      PotentialConsequence <|-- Benefit
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Benefit
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Benefit
        click PotentialRisk href "../PotentialRisk/"
      Compensation <|-- Benefit
        click Compensation href "../Compensation/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [FinancialImpact](FinancialImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Remuneration](Remuneration.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Compensation](Compensation.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * **Benefit** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Benefit](https://w3id.org/lmodel/dpv/risk/Benefit) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Benefit


## Comments

* Even though benefits is filed under organisational concepts, it can be
applied to individuals (humans) and groups which are societal



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Benefit |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Benefit |
| native | risk:Benefit |
| exact | dpv_risk:Benefit, dpv_risk_owl:Benefit |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Benefit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Benefit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing benefits - both material and immaterial
comments:
- 'Even though benefits is filed under organisational concepts, it can be

  applied to individuals (humans) and groups which are societal'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Benefit
exact_mappings:
- dpv_risk:Benefit
- dpv_risk_owl:Benefit
is_a: Compensation
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Benefit

```
</details>

### Induced

<details>
```yaml
name: Benefit
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Benefit
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing benefits - both material and immaterial
comments:
- 'Even though benefits is filed under organisational concepts, it can be

  applied to individuals (humans) and groups which are societal'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Benefit
exact_mappings:
- dpv_risk:Benefit
- dpv_risk_owl:Benefit
is_a: Compensation
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Benefit

```
</details></div>