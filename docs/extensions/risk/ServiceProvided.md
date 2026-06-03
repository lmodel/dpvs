---
search:
  boost: 10.0
---

# Class: ServiceProvided 


_Concept representing service provided_



<div data-search-exclude markdown="1">



URI: [risk:ServiceProvided](https://w3id.org/lmodel/dpv/risk/ServiceProvided)





```mermaid
 classDiagram
    class ServiceProvided
    click ServiceProvided href "../ServiceProvided/"
      PotentialConsequence <|-- ServiceProvided
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceProvided
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceProvided
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceProvided
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceProvided** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceProvided](https://w3id.org/lmodel/dpv/risk/ServiceProvided) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Provided




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceProvided |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceProvided |
| native | risk:ServiceProvided |
| exact | dpv_risk:ServiceProvided, dpv_risk_owl:ServiceProvided |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service provided
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Provided
exact_mappings:
- dpv_risk:ServiceProvided
- dpv_risk_owl:ServiceProvided
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceProvided

```
</details>

### Induced

<details>
```yaml
name: ServiceProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service provided
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Provided
exact_mappings:
- dpv_risk:ServiceProvided
- dpv_risk_owl:ServiceProvided
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceProvided

```
</details></div>