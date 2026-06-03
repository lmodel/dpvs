---
search:
  boost: 10.0
---

# Class: PublicServicesExclusion 


_Concept representing exclusion from public services_



<div data-search-exclude markdown="1">



URI: [risk:PublicServicesExclusion](https://w3id.org/lmodel/dpv/risk/PublicServicesExclusion)





```mermaid
 classDiagram
    class PublicServicesExclusion
    click PublicServicesExclusion href "../PublicServicesExclusion/"
      PotentialConsequence <|-- PublicServicesExclusion
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PublicServicesExclusion
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PublicServicesExclusion
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- PublicServicesExclusion
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **PublicServicesExclusion** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PublicServicesExclusion](https://w3id.org/lmodel/dpv/risk/PublicServicesExclusion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Public Services Exclusion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PublicServicesExclusion |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PublicServicesExclusion |
| native | risk:PublicServicesExclusion |
| exact | dpv_risk:PublicServicesExclusion, dpv_risk_owl:PublicServicesExclusion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PublicServicesExclusion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PublicServicesExclusion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing exclusion from public services
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Public Services Exclusion
exact_mappings:
- dpv_risk:PublicServicesExclusion
- dpv_risk_owl:PublicServicesExclusion
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PublicServicesExclusion

```
</details>

### Induced

<details>
```yaml
name: PublicServicesExclusion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PublicServicesExclusion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing exclusion from public services
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Public Services Exclusion
exact_mappings:
- dpv_risk:PublicServicesExclusion
- dpv_risk_owl:PublicServicesExclusion
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PublicServicesExclusion

```
</details></div>