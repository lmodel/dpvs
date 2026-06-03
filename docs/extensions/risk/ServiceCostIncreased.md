---
search:
  boost: 10.0
---

# Class: ServiceCostIncreased 


_Concept representing service cost increased_



<div data-search-exclude markdown="1">



URI: [risk:ServiceCostIncreased](https://w3id.org/lmodel/dpv/risk/ServiceCostIncreased)





```mermaid
 classDiagram
    class ServiceCostIncreased
    click ServiceCostIncreased href "../ServiceCostIncreased/"
      PotentialConsequence <|-- ServiceCostIncreased
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceCostIncreased
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceCostIncreased
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceCostIncreased
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceCostIncreased** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceCostIncreased](https://w3id.org/lmodel/dpv/risk/ServiceCostIncreased) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Cost Increased




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceCostIncreased |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceCostIncreased |
| native | risk:ServiceCostIncreased |
| exact | dpv_risk:ServiceCostIncreased, dpv_risk_owl:ServiceCostIncreased |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceCostIncreased
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceCostIncreased
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service cost increased
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Cost Increased
exact_mappings:
- dpv_risk:ServiceCostIncreased
- dpv_risk_owl:ServiceCostIncreased
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceCostIncreased

```
</details>

### Induced

<details>
```yaml
name: ServiceCostIncreased
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceCostIncreased
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service cost increased
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Cost Increased
exact_mappings:
- dpv_risk:ServiceCostIncreased
- dpv_risk_owl:ServiceCostIncreased
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceCostIncreased

```
</details></div>