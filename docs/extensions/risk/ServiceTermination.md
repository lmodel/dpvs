---
search:
  boost: 10.0
---

# Class: ServiceTermination 


_Concept representing service termination_



<div data-search-exclude markdown="1">



URI: [risk:ServiceTermination](https://w3id.org/lmodel/dpv/risk/ServiceTermination)





```mermaid
 classDiagram
    class ServiceTermination
    click ServiceTermination href "../ServiceTermination/"
      PotentialConsequence <|-- ServiceTermination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceTermination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceTermination
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceTermination
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceTermination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceTermination](https://w3id.org/lmodel/dpv/risk/ServiceTermination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Termination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceTermination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceTermination |
| native | risk:ServiceTermination |
| exact | dpv_risk:ServiceTermination, dpv_risk_owl:ServiceTermination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceTermination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceTermination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service termination
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Termination
exact_mappings:
- dpv_risk:ServiceTermination
- dpv_risk_owl:ServiceTermination
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceTermination

```
</details>

### Induced

<details>
```yaml
name: ServiceTermination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceTermination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service termination
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Termination
exact_mappings:
- dpv_risk:ServiceTermination
- dpv_risk_owl:ServiceTermination
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceTermination

```
</details></div>