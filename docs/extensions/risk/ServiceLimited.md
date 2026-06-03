---
search:
  boost: 10.0
---

# Class: ServiceLimited 


_Concept representing service limited_



<div data-search-exclude markdown="1">



URI: [risk:ServiceLimited](https://w3id.org/lmodel/dpv/risk/ServiceLimited)





```mermaid
 classDiagram
    class ServiceLimited
    click ServiceLimited href "../ServiceLimited/"
      PotentialConsequence <|-- ServiceLimited
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceLimited
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceLimited
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceLimited
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceLimited** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceLimited](https://w3id.org/lmodel/dpv/risk/ServiceLimited) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Limited




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceLimited |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceLimited |
| native | risk:ServiceLimited |
| exact | dpv_risk:ServiceLimited, dpv_risk_owl:ServiceLimited |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceLimited
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceLimited
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service limited
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Limited
exact_mappings:
- dpv_risk:ServiceLimited
- dpv_risk_owl:ServiceLimited
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceLimited

```
</details>

### Induced

<details>
```yaml
name: ServiceLimited
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceLimited
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service limited
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Limited
exact_mappings:
- dpv_risk:ServiceLimited
- dpv_risk_owl:ServiceLimited
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceLimited

```
</details></div>