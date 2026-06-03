---
search:
  boost: 10.0
---

# Class: ServiceQualityReduced 


_Concept representing service quality reduced_



<div data-search-exclude markdown="1">



URI: [risk:ServiceQualityReduced](https://w3id.org/lmodel/dpv/risk/ServiceQualityReduced)





```mermaid
 classDiagram
    class ServiceQualityReduced
    click ServiceQualityReduced href "../ServiceQualityReduced/"
      PotentialConsequence <|-- ServiceQualityReduced
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceQualityReduced
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceQualityReduced
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceQualityReduced
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceQualityReduced** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceQualityReduced](https://w3id.org/lmodel/dpv/risk/ServiceQualityReduced) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Quality Reduced




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceQualityReduced |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceQualityReduced |
| native | risk:ServiceQualityReduced |
| exact | dpv_risk:ServiceQualityReduced, dpv_risk_owl:ServiceQualityReduced |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceQualityReduced
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceQualityReduced
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service quality reduced
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Quality Reduced
exact_mappings:
- dpv_risk:ServiceQualityReduced
- dpv_risk_owl:ServiceQualityReduced
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceQualityReduced

```
</details>

### Induced

<details>
```yaml
name: ServiceQualityReduced
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceQualityReduced
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service quality reduced
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Quality Reduced
exact_mappings:
- dpv_risk:ServiceQualityReduced
- dpv_risk_owl:ServiceQualityReduced
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceQualityReduced

```
</details></div>