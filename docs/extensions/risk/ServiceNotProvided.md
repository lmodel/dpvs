---
search:
  boost: 10.0
---

# Class: ServiceNotProvided 


_Concept representing service not provided_



<div data-search-exclude markdown="1">



URI: [risk:ServiceNotProvided](https://w3id.org/lmodel/dpv/risk/ServiceNotProvided)





```mermaid
 classDiagram
    class ServiceNotProvided
    click ServiceNotProvided href "../ServiceNotProvided/"
      PotentialConsequence <|-- ServiceNotProvided
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceNotProvided
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceNotProvided
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceNotProvided
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceNotProvided** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceNotProvided](https://w3id.org/lmodel/dpv/risk/ServiceNotProvided) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Not Provided




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceNotProvided |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceNotProvided |
| native | risk:ServiceNotProvided |
| exact | dpv_risk:ServiceNotProvided, dpv_risk_owl:ServiceNotProvided |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceNotProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceNotProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service not provided
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Not Provided
exact_mappings:
- dpv_risk:ServiceNotProvided
- dpv_risk_owl:ServiceNotProvided
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceNotProvided

```
</details>

### Induced

<details>
```yaml
name: ServiceNotProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceNotProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service not provided
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Not Provided
exact_mappings:
- dpv_risk:ServiceNotProvided
- dpv_risk_owl:ServiceNotProvided
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceNotProvided

```
</details></div>