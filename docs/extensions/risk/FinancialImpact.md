---
search:
  boost: 10.0
---

# Class: FinancialImpact 


_Things that cause or have the potential to impact financial resources_



<div data-search-exclude markdown="1">



URI: [risk:FinancialImpact](https://w3id.org/lmodel/dpv/risk/FinancialImpact)





```mermaid
 classDiagram
    class FinancialImpact
    click FinancialImpact href "../FinancialImpact/"
      PotentialConsequence <|-- FinancialImpact
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- FinancialImpact
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- FinancialImpact
        click PotentialRisk href "../PotentialRisk/"
      OrganisationalRiskConcept <|-- FinancialImpact
        click OrganisationalRiskConcept href "../OrganisationalRiskConcept/"
      

      FinancialImpact <|-- FinancialLoss
        click FinancialLoss href "../FinancialLoss/"
      FinancialImpact <|-- Remuneration
        click Remuneration href "../Remuneration/"
      

      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **FinancialImpact** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [FinancialLoss](FinancialLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [Remuneration](Remuneration.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:FinancialImpact](https://w3id.org/lmodel/dpv/risk/FinancialImpact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Financial Impact




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#FinancialImpact |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:FinancialImpact |
| native | risk:FinancialImpact |
| exact | dpv_risk:FinancialImpact, dpv_risk_owl:FinancialImpact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FinancialImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#FinancialImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Things that cause or have the potential to impact financial resources
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Financial Impact
exact_mappings:
- dpv_risk:FinancialImpact
- dpv_risk_owl:FinancialImpact
is_a: OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:FinancialImpact

```
</details>

### Induced

<details>
```yaml
name: FinancialImpact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#FinancialImpact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Things that cause or have the potential to impact financial resources
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Financial Impact
exact_mappings:
- dpv_risk:FinancialImpact
- dpv_risk_owl:FinancialImpact
is_a: OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:FinancialImpact

```
</details></div>