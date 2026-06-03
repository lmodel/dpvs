---
search:
  boost: 10.0
---

# Class: FinancialLoss 


_Concept representing Financial Loss which may be actual loss of existing_

_financial assets or hypothetical loss of financial opportunity_



<div data-search-exclude markdown="1">



URI: [risk:FinancialLoss](https://w3id.org/lmodel/dpv/risk/FinancialLoss)





```mermaid
 classDiagram
    class FinancialLoss
    click FinancialLoss href "../FinancialLoss/"
      PotentialConsequence <|-- FinancialLoss
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- FinancialLoss
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- FinancialLoss
        click PotentialRisk href "../PotentialRisk/"
      FinancialImpact <|-- FinancialLoss
        click FinancialImpact href "../FinancialImpact/"
      

      FinancialLoss <|-- JudicialCosts
        click JudicialCosts href "../JudicialCosts/"
      FinancialLoss <|-- JudicialPenalty
        click JudicialPenalty href "../JudicialPenalty/"
      

      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [FinancialImpact](FinancialImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **FinancialLoss** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [JudicialCosts](JudicialCosts.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [JudicialPenalty](JudicialPenalty.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:FinancialLoss](https://w3id.org/lmodel/dpv/risk/FinancialLoss) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Financial Loss




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#FinancialLoss |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:FinancialLoss |
| native | risk:FinancialLoss |
| exact | dpv_risk:FinancialLoss, dpv_risk_owl:FinancialLoss |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FinancialLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#FinancialLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing Financial Loss which may be actual loss of existing

  financial assets or hypothetical loss of financial opportunity'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Financial Loss
exact_mappings:
- dpv_risk:FinancialLoss
- dpv_risk_owl:FinancialLoss
is_a: FinancialImpact
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:FinancialLoss

```
</details>

### Induced

<details>
```yaml
name: FinancialLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#FinancialLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing Financial Loss which may be actual loss of existing

  financial assets or hypothetical loss of financial opportunity'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Financial Loss
exact_mappings:
- dpv_risk:FinancialLoss
- dpv_risk_owl:FinancialLoss
is_a: FinancialImpact
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:FinancialLoss

```
</details></div>