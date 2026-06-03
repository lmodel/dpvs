---
search:
  boost: 10.0
---

# Class: ServiceAlternativeOffered 


_Concept representing service alternative offered_



<div data-search-exclude markdown="1">



URI: [risk:ServiceAlternativeOffered](https://w3id.org/lmodel/dpv/risk/ServiceAlternativeOffered)





```mermaid
 classDiagram
    class ServiceAlternativeOffered
    click ServiceAlternativeOffered href "../ServiceAlternativeOffered/"
      PotentialConsequence <|-- ServiceAlternativeOffered
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceAlternativeOffered
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceAlternativeOffered
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceAlternativeOffered
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceAlternativeOffered** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceAlternativeOffered](https://w3id.org/lmodel/dpv/risk/ServiceAlternativeOffered) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Alternative Offered




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceAlternativeOffered |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceAlternativeOffered |
| native | risk:ServiceAlternativeOffered |
| exact | dpv_risk:ServiceAlternativeOffered, dpv_risk_owl:ServiceAlternativeOffered |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceAlternativeOffered
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceAlternativeOffered
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service alternative offered
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Alternative Offered
exact_mappings:
- dpv_risk:ServiceAlternativeOffered
- dpv_risk_owl:ServiceAlternativeOffered
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceAlternativeOffered

```
</details>

### Induced

<details>
```yaml
name: ServiceAlternativeOffered
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceAlternativeOffered
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service alternative offered
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Alternative Offered
exact_mappings:
- dpv_risk:ServiceAlternativeOffered
- dpv_risk_owl:ServiceAlternativeOffered
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceAlternativeOffered

```
</details></div>