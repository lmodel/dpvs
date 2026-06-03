---
search:
  boost: 10.0
---

# Class: JudicialPenalty 


_Something that involves or causes judicial penalties to be paid_



<div data-search-exclude markdown="1">



URI: [risk:JudicialPenalty](https://w3id.org/lmodel/dpv/risk/JudicialPenalty)





```mermaid
 classDiagram
    class JudicialPenalty
    click JudicialPenalty href "../JudicialPenalty/"
      PotentialConsequence <|-- JudicialPenalty
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- JudicialPenalty
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- JudicialPenalty
        click PotentialRisk href "../PotentialRisk/"
      FinancialLoss <|-- JudicialPenalty
        click FinancialLoss href "../FinancialLoss/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [FinancialImpact](FinancialImpact.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [FinancialLoss](FinancialLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **JudicialPenalty** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:JudicialPenalty](https://w3id.org/lmodel/dpv/risk/JudicialPenalty) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Judicial Penalty




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#JudicialPenalty |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:JudicialPenalty |
| native | risk:JudicialPenalty |
| exact | dpv_risk:JudicialPenalty, dpv_risk_owl:JudicialPenalty |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: JudicialPenalty
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#JudicialPenalty
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Something that involves or causes judicial penalties to be paid
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Judicial Penalty
exact_mappings:
- dpv_risk:JudicialPenalty
- dpv_risk_owl:JudicialPenalty
is_a: FinancialLoss
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:JudicialPenalty

```
</details>

### Induced

<details>
```yaml
name: JudicialPenalty
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#JudicialPenalty
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Something that involves or causes judicial penalties to be paid
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Judicial Penalty
exact_mappings:
- dpv_risk:JudicialPenalty
- dpv_risk_owl:JudicialPenalty
is_a: FinancialLoss
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:JudicialPenalty

```
</details></div>