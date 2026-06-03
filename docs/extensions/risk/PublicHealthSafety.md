---
search:
  boost: 10.0
---

# Class: PublicHealthSafety 


_Concept representing health and safety of the public at large_



<div data-search-exclude markdown="1">



URI: [risk:PublicHealthSafety](https://w3id.org/lmodel/dpv/risk/PublicHealthSafety)





```mermaid
 classDiagram
    class PublicHealthSafety
    click PublicHealthSafety href "../PublicHealthSafety/"
      PotentialConsequence <|-- PublicHealthSafety
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PublicHealthSafety
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PublicHealthSafety
        click PotentialRisk href "../PotentialRisk/"
      HealthSafety <|-- PublicHealthSafety
        click HealthSafety href "../HealthSafety/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **PublicHealthSafety** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PublicHealthSafety](https://w3id.org/lmodel/dpv/risk/PublicHealthSafety) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Public Health & Safety




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PublicHealthSafety |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PublicHealthSafety |
| native | risk:PublicHealthSafety |
| exact | dpv_risk:PublicHealthSafety, dpv_risk_owl:PublicHealthSafety |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PublicHealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PublicHealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing health and safety of the public at large
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Public Health & Safety
exact_mappings:
- dpv_risk:PublicHealthSafety
- dpv_risk_owl:PublicHealthSafety
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PublicHealthSafety

```
</details>

### Induced

<details>
```yaml
name: PublicHealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PublicHealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing health and safety of the public at large
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Public Health & Safety
exact_mappings:
- dpv_risk:PublicHealthSafety
- dpv_risk_owl:PublicHealthSafety
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PublicHealthSafety

```
</details></div>