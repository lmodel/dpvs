---
search:
  boost: 10.0
---

# Class: Compensation 


_Something that acts as or provides compensation - which can be monetary_

_and financial or in other forms_



<div data-search-exclude markdown="1">



URI: [risk:Compensation](https://w3id.org/lmodel/dpv/risk/Compensation)





```mermaid
 classDiagram
    class Compensation
    click Compensation href "../Compensation/"
      PotentialConsequence <|-- Compensation
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Compensation
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Compensation
        click PotentialRisk href "../PotentialRisk/"
      Remuneration <|-- Compensation
        click Remuneration href "../Remuneration/"
      

      Compensation <|-- Benefit
        click Benefit href "../Benefit/"
      

      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [FinancialImpact](FinancialImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Remuneration](Remuneration.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **Compensation** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * [Benefit](Benefit.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Compensation](https://w3id.org/lmodel/dpv/risk/Compensation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Compensation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Compensation |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Compensation |
| native | risk:Compensation |
| exact | dpv_risk:Compensation, dpv_risk_owl:Compensation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Compensation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Compensation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as or provides compensation - which can be monetary

  and financial or in other forms'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Compensation
exact_mappings:
- dpv_risk:Compensation
- dpv_risk_owl:Compensation
is_a: Remuneration
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Compensation

```
</details>

### Induced

<details>
```yaml
name: Compensation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Compensation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as or provides compensation - which can be monetary

  and financial or in other forms'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Compensation
exact_mappings:
- dpv_risk:Compensation
- dpv_risk_owl:Compensation
is_a: Remuneration
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Compensation

```
</details></div>