---
search:
  boost: 10.0
---

# Class: JudicialCosts 


_Something that involves or causes judicial costs to be paid_



<div data-search-exclude markdown="1">



URI: [risk:JudicialCosts](https://w3id.org/lmodel/dpv/risk/JudicialCosts)





```mermaid
 classDiagram
    class JudicialCosts
    click JudicialCosts href "../JudicialCosts/"
      PotentialConsequence <|-- JudicialCosts
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- JudicialCosts
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- JudicialCosts
        click PotentialRisk href "../PotentialRisk/"
      FinancialLoss <|-- JudicialCosts
        click FinancialLoss href "../FinancialLoss/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [FinancialImpact](FinancialImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [FinancialLoss](FinancialLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **JudicialCosts** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:JudicialCosts](https://w3id.org/lmodel/dpv/risk/JudicialCosts) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Judicial Costs




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#JudicialCosts |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:JudicialCosts |
| native | risk:JudicialCosts |
| exact | dpv_risk:JudicialCosts, dpv_risk_owl:JudicialCosts |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: JudicialCosts
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#JudicialCosts
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Something that involves or causes judicial costs to be paid
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Judicial Costs
exact_mappings:
- dpv_risk:JudicialCosts
- dpv_risk_owl:JudicialCosts
is_a: FinancialLoss
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:JudicialCosts

```
</details>

### Induced

<details>
```yaml
name: JudicialCosts
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#JudicialCosts
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Something that involves or causes judicial costs to be paid
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Judicial Costs
exact_mappings:
- dpv_risk:JudicialCosts
- dpv_risk_owl:JudicialCosts
is_a: FinancialLoss
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:JudicialCosts

```
</details></div>