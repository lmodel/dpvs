---
search:
  boost: 10.0
---

# Class: ReputationalLoss 


_Concept representing Reputational Loss_



<div data-search-exclude markdown="1">



URI: [risk:ReputationalLoss](https://w3id.org/lmodel/dpv/risk/ReputationalLoss)





```mermaid
 classDiagram
    class ReputationalLoss
    click ReputationalLoss href "../ReputationalLoss/"
      PotentialConsequence <|-- ReputationalLoss
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ReputationalLoss
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ReputationalLoss
        click PotentialRisk href "../PotentialRisk/"
      ReputationalRisk <|-- ReputationalLoss
        click ReputationalRisk href "../ReputationalRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ReputationalRisk](ReputationalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ReputationalLoss** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ReputationalLoss](https://w3id.org/lmodel/dpv/risk/ReputationalLoss) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Reputational Loss




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ReputationalLoss |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ReputationalLoss |
| native | risk:ReputationalLoss |
| exact | dpv_risk:ReputationalLoss, dpv_risk_owl:ReputationalLoss |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReputationalLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReputationalLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Reputational Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reputational Loss
exact_mappings:
- dpv_risk:ReputationalLoss
- dpv_risk_owl:ReputationalLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ReputationalLoss

```
</details>

### Induced

<details>
```yaml
name: ReputationalLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReputationalLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Reputational Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reputational Loss
exact_mappings:
- dpv_risk:ReputationalLoss
- dpv_risk_owl:ReputationalLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ReputationalLoss

```
</details></div>