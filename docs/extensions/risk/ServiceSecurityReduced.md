---
search:
  boost: 10.0
---

# Class: ServiceSecurityReduced 


_Concept representing service security reduced_



<div data-search-exclude markdown="1">



URI: [risk:ServiceSecurityReduced](https://w3id.org/lmodel/dpv/risk/ServiceSecurityReduced)





```mermaid
 classDiagram
    class ServiceSecurityReduced
    click ServiceSecurityReduced href "../ServiceSecurityReduced/"
      PotentialConsequence <|-- ServiceSecurityReduced
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceSecurityReduced
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceSecurityReduced
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceSecurityReduced
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceSecurityReduced** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceSecurityReduced](https://w3id.org/lmodel/dpv/risk/ServiceSecurityReduced) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Security Reduced




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceSecurityReduced |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceSecurityReduced |
| native | risk:ServiceSecurityReduced |
| exact | dpv_risk:ServiceSecurityReduced, dpv_risk_owl:ServiceSecurityReduced |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceSecurityReduced
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceSecurityReduced
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service security reduced
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Security Reduced
exact_mappings:
- dpv_risk:ServiceSecurityReduced
- dpv_risk_owl:ServiceSecurityReduced
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceSecurityReduced

```
</details>

### Induced

<details>
```yaml
name: ServiceSecurityReduced
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceSecurityReduced
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service security reduced
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Security Reduced
exact_mappings:
- dpv_risk:ServiceSecurityReduced
- dpv_risk_owl:ServiceSecurityReduced
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceSecurityReduced

```
</details></div>