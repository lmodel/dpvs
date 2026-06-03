---
search:
  boost: 10.0
---

# Class: TrustLoss 


_Concept representing Trust Loss_



<div data-search-exclude markdown="1">



URI: [risk:TrustLoss](https://w3id.org/lmodel/dpv/risk/TrustLoss)





```mermaid
 classDiagram
    class TrustLoss
    click TrustLoss href "../TrustLoss/"
      PotentialConsequence <|-- TrustLoss
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- TrustLoss
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- TrustLoss
        click PotentialRisk href "../PotentialRisk/"
      ReputationalRisk <|-- TrustLoss
        click ReputationalRisk href "../ReputationalRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ReputationalRisk](ReputationalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **TrustLoss** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:TrustLoss](https://w3id.org/lmodel/dpv/risk/TrustLoss) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Trust Loss




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#TrustLoss |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:TrustLoss |
| native | risk:TrustLoss |
| exact | dpv_risk:TrustLoss, dpv_risk_owl:TrustLoss |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TrustLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TrustLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Trust Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Trust Loss
exact_mappings:
- dpv_risk:TrustLoss
- dpv_risk_owl:TrustLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:TrustLoss

```
</details>

### Induced

<details>
```yaml
name: TrustLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TrustLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Trust Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Trust Loss
exact_mappings:
- dpv_risk:TrustLoss
- dpv_risk_owl:TrustLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:TrustLoss

```
</details></div>