---
search:
  boost: 10.0
---

# Class: IndividualHealthSafety 


_Concept representing health & safety of individual(s)_



<div data-search-exclude markdown="1">



URI: [risk:IndividualHealthSafety](https://w3id.org/lmodel/dpv/risk/IndividualHealthSafety)





```mermaid
 classDiagram
    class IndividualHealthSafety
    click IndividualHealthSafety href "../IndividualHealthSafety/"
      PotentialConsequence <|-- IndividualHealthSafety
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- IndividualHealthSafety
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- IndividualHealthSafety
        click PotentialRisk href "../PotentialRisk/"
      IndividualRisk <|-- IndividualHealthSafety
        click IndividualRisk href "../IndividualRisk/"
      HealthSafety <|-- IndividualHealthSafety
        click HealthSafety href "../HealthSafety/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * **IndividualHealthSafety** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [IndividualRisk](IndividualRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IndividualHealthSafety](https://w3id.org/lmodel/dpv/risk/IndividualHealthSafety) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Individual Health & Safety




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IndividualHealthSafety |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IndividualHealthSafety |
| native | risk:IndividualHealthSafety |
| exact | dpv_risk:IndividualHealthSafety, dpv_risk_owl:IndividualHealthSafety |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IndividualHealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IndividualHealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing health & safety of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Individual Health & Safety
exact_mappings:
- dpv_risk:IndividualHealthSafety
- dpv_risk_owl:IndividualHealthSafety
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- IndividualRisk
class_uri: risk:IndividualHealthSafety

```
</details>

### Induced

<details>
```yaml
name: IndividualHealthSafety
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IndividualHealthSafety
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing health & safety of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Individual Health & Safety
exact_mappings:
- dpv_risk:IndividualHealthSafety
- dpv_risk_owl:IndividualHealthSafety
is_a: HealthSafety
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- IndividualRisk
class_uri: risk:IndividualHealthSafety

```
</details></div>