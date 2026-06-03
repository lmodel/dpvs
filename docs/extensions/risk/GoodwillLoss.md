---
search:
  boost: 10.0
---

# Class: GoodwillLoss 


_Concept representing Goodwill Loss_



<div data-search-exclude markdown="1">



URI: [risk:GoodwillLoss](https://w3id.org/lmodel/dpv/risk/GoodwillLoss)





```mermaid
 classDiagram
    class GoodwillLoss
    click GoodwillLoss href "../GoodwillLoss/"
      PotentialConsequence <|-- GoodwillLoss
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- GoodwillLoss
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- GoodwillLoss
        click PotentialRisk href "../PotentialRisk/"
      ReputationalRisk <|-- GoodwillLoss
        click ReputationalRisk href "../ReputationalRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ReputationalRisk](ReputationalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **GoodwillLoss** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:GoodwillLoss](https://w3id.org/lmodel/dpv/risk/GoodwillLoss) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Goodwill Loss




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#GoodwillLoss |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:GoodwillLoss |
| native | risk:GoodwillLoss |
| exact | dpv_risk:GoodwillLoss, dpv_risk_owl:GoodwillLoss |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GoodwillLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GoodwillLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Goodwill Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Goodwill Loss
exact_mappings:
- dpv_risk:GoodwillLoss
- dpv_risk_owl:GoodwillLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:GoodwillLoss

```
</details>

### Induced

<details>
```yaml
name: GoodwillLoss
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GoodwillLoss
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Goodwill Loss
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Goodwill Loss
exact_mappings:
- dpv_risk:GoodwillLoss
- dpv_risk_owl:GoodwillLoss
is_a: ReputationalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:GoodwillLoss

```
</details></div>