---
search:
  boost: 10.0
---

# Class: ServiceDenied 


_Concept representing service denied_



<div data-search-exclude markdown="1">



URI: [risk:ServiceDenied](https://w3id.org/lmodel/dpv/risk/ServiceDenied)





```mermaid
 classDiagram
    class ServiceDenied
    click ServiceDenied href "../ServiceDenied/"
      PotentialConsequence <|-- ServiceDenied
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceDenied
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceDenied
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceDenied
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceDenied** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceDenied](https://w3id.org/lmodel/dpv/risk/ServiceDenied) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Denied




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceDenied |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceDenied |
| native | risk:ServiceDenied |
| exact | dpv_risk:ServiceDenied, dpv_risk_owl:ServiceDenied |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceDenied
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceDenied
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service denied
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Denied
exact_mappings:
- dpv_risk:ServiceDenied
- dpv_risk_owl:ServiceDenied
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceDenied

```
</details>

### Induced

<details>
```yaml
name: ServiceDenied
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceDenied
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service denied
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Denied
exact_mappings:
- dpv_risk:ServiceDenied
- dpv_risk_owl:ServiceDenied
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceDenied

```
</details></div>