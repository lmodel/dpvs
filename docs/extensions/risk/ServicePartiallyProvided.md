---
search:
  boost: 10.0
---

# Class: ServicePartiallyProvided 


_Concept representing service partially provided_



<div data-search-exclude markdown="1">



URI: [risk:ServicePartiallyProvided](https://w3id.org/lmodel/dpv/risk/ServicePartiallyProvided)





```mermaid
 classDiagram
    class ServicePartiallyProvided
    click ServicePartiallyProvided href "../ServicePartiallyProvided/"
      PotentialConsequence <|-- ServicePartiallyProvided
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServicePartiallyProvided
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServicePartiallyProvided
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServicePartiallyProvided
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServicePartiallyProvided** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServicePartiallyProvided](https://w3id.org/lmodel/dpv/risk/ServicePartiallyProvided) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Partially Provided




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServicePartiallyProvided |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServicePartiallyProvided |
| native | risk:ServicePartiallyProvided |
| exact | dpv_risk:ServicePartiallyProvided, dpv_risk_owl:ServicePartiallyProvided |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServicePartiallyProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServicePartiallyProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service partially provided
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Partially Provided
exact_mappings:
- dpv_risk:ServicePartiallyProvided
- dpv_risk_owl:ServicePartiallyProvided
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServicePartiallyProvided

```
</details>

### Induced

<details>
```yaml
name: ServicePartiallyProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServicePartiallyProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service partially provided
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Partially Provided
exact_mappings:
- dpv_risk:ServicePartiallyProvided
- dpv_risk_owl:ServicePartiallyProvided
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServicePartiallyProvided

```
</details></div>