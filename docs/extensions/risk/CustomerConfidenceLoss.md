---
search:
  boost: 10.0
---

# Class: CustomerConfidenceLoss 


_Concept representing Customer Confidence Loss_



<div data-search-exclude markdown="1">



URI: [risk:CustomerConfidenceLoss](https://w3id.org/lmodel/dpv/risk/CustomerConfidenceLoss)





```mermaid
 classDiagram
    class CustomerConfidenceLoss
    click CustomerConfidenceLoss href "../CustomerConfidenceLoss/"
      PotentialConsequence <|-- CustomerConfidenceLoss
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- CustomerConfidenceLoss
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- CustomerConfidenceLoss
        click PotentialRisk href "../PotentialRisk/"
      ReputationalRisk <|-- CustomerConfidenceLoss
        click ReputationalRisk href "../ReputationalRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ReputationalRisk](ReputationalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **CustomerConfidenceLoss** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CustomerConfidenceLoss](https://w3id.org/lmodel/dpv/risk/CustomerConfidenceLoss) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Customer Confidence Loss




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#CustomerConfidenceLoss |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CustomerConfidenceLoss |
| native | risk:CustomerConfidenceLoss |
| exact | dpv_risk:CustomerConfidenceLoss, dpv_risk_owl:CustomerConfidenceLoss |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CustomerConfidenceLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CustomerConfidenceLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Customer Confidence Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Customer Confidence Loss
exact_mappings:
- dpv_risk:CustomerConfidenceLoss
- dpv_risk_owl:CustomerConfidenceLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:CustomerConfidenceLoss

```
</details>

### Induced

<details>
```yaml
name: CustomerConfidenceLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CustomerConfidenceLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Customer Confidence Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Customer Confidence Loss
exact_mappings:
- dpv_risk:CustomerConfidenceLoss
- dpv_risk_owl:CustomerConfidenceLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:CustomerConfidenceLoss

```
</details></div>