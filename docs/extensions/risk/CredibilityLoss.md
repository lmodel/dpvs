---
search:
  boost: 10.0
---

# Class: CredibilityLoss 


_Concept representing Credibility Loss_



<div data-search-exclude markdown="1">



URI: [risk:CredibilityLoss](https://w3id.org/lmodel/dpv/risk/CredibilityLoss)





```mermaid
 classDiagram
    class CredibilityLoss
    click CredibilityLoss href "../CredibilityLoss/"
      PotentialConsequence <|-- CredibilityLoss
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- CredibilityLoss
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- CredibilityLoss
        click PotentialRisk href "../PotentialRisk/"
      ReputationalRisk <|-- CredibilityLoss
        click ReputationalRisk href "../ReputationalRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ReputationalRisk](ReputationalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **CredibilityLoss** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CredibilityLoss](https://w3id.org/lmodel/dpv/risk/CredibilityLoss) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Credibility Loss




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#CredibilityLoss |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CredibilityLoss |
| native | risk:CredibilityLoss |
| exact | dpv_risk:CredibilityLoss, dpv_risk_owl:CredibilityLoss |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CredibilityLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CredibilityLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Credibility Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Credibility Loss
exact_mappings:
- dpv_risk:CredibilityLoss
- dpv_risk_owl:CredibilityLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:CredibilityLoss

```
</details>

### Induced

<details>
```yaml
name: CredibilityLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CredibilityLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Credibility Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Credibility Loss
exact_mappings:
- dpv_risk:CredibilityLoss
- dpv_risk_owl:CredibilityLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:CredibilityLoss

```
</details></div>