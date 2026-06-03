---
search:
  boost: 10.0
---

# Class: Remuneration 


_Something that acts as or provides remuneration which is in monetary or_

_financial form_



<div data-search-exclude markdown="1">



URI: [risk:Remuneration](https://w3id.org/lmodel/dpv/risk/Remuneration)





```mermaid
 classDiagram
    class Remuneration
    click Remuneration href "../Remuneration/"
      PotentialConsequence <|-- Remuneration
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Remuneration
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Remuneration
        click PotentialRisk href "../PotentialRisk/"
      FinancialImpact <|-- Remuneration
        click FinancialImpact href "../FinancialImpact/"
      

      Remuneration <|-- Compensation
        click Compensation href "../Compensation/"
      Remuneration <|-- Payment
        click Payment href "../Payment/"
      Remuneration <|-- Reward
        click Reward href "../Reward/"
      

      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [FinancialImpact](FinancialImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **Remuneration** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Compensation](Compensation.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Payment](Payment.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Reward](Reward.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Remuneration](https://w3id.org/lmodel/dpv/risk/Remuneration) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Remuneration




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Remuneration |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Remuneration |
| native | risk:Remuneration |
| exact | dpv_risk:Remuneration, dpv_risk_owl:Remuneration |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Remuneration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Remuneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as or provides remuneration which is in monetary
  or

  financial form'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Remuneration
exact_mappings:
- dpv_risk:Remuneration
- dpv_risk_owl:Remuneration
is_a: FinancialImpact
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Remuneration

```
</details>

### Induced

<details>
```yaml
name: Remuneration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Remuneration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Something that acts as or provides remuneration which is in monetary
  or

  financial form'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Remuneration
exact_mappings:
- dpv_risk:Remuneration
- dpv_risk_owl:Remuneration
is_a: FinancialImpact
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Remuneration

```
</details></div>