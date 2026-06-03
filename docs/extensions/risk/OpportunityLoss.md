---
search:
  boost: 10.0
---

# Class: OpportunityLoss 


_Concept representing Opportunity Loss_



<div data-search-exclude markdown="1">



URI: [risk:OpportunityLoss](https://w3id.org/lmodel/dpv/risk/OpportunityLoss)





```mermaid
 classDiagram
    class OpportunityLoss
    click OpportunityLoss href "../OpportunityLoss/"
      PotentialConsequence <|-- OpportunityLoss
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- OpportunityLoss
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- OpportunityLoss
        click PotentialRisk href "../PotentialRisk/"
      ReputationalRisk <|-- OpportunityLoss
        click ReputationalRisk href "../ReputationalRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ReputationalRisk](ReputationalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **OpportunityLoss** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:OpportunityLoss](https://w3id.org/lmodel/dpv/risk/OpportunityLoss) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Opportunity Loss




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#OpportunityLoss |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:OpportunityLoss |
| native | risk:OpportunityLoss |
| exact | dpv_risk:OpportunityLoss, dpv_risk_owl:OpportunityLoss |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OpportunityLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OpportunityLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Opportunity Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Opportunity Loss
exact_mappings:
- dpv_risk:OpportunityLoss
- dpv_risk_owl:OpportunityLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:OpportunityLoss

```
</details>

### Induced

<details>
```yaml
name: OpportunityLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#OpportunityLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Opportunity Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Opportunity Loss
exact_mappings:
- dpv_risk:OpportunityLoss
- dpv_risk_owl:OpportunityLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:OpportunityLoss

```
</details></div>