---
search:
  boost: 10.0
---

# Class: Reidentification 


_Concept representing Re-identification_



<div data-search-exclude markdown="1">



URI: [risk:Reidentification](https://w3id.org/lmodel/dpv/risk/Reidentification)





```mermaid
 classDiagram
    class Reidentification
    click Reidentification href "../Reidentification/"
      ConfidentialityConcept <|-- Reidentification
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- Reidentification
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Reidentification
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Reidentification
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- Reidentification
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **Reidentification** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Reidentification](https://w3id.org/lmodel/dpv/risk/Reidentification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Re-identification


## Comments

* Use this concept for reidentification in an internal context. For
reidentification performed by external entities see concept
UnauthorisedReidentification



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Reidentification |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Reidentification |
| native | risk:Reidentification |
| exact | dpv_risk:Reidentification, dpv_risk_owl:Reidentification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Reidentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Reidentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Re-identification
comments:
- 'Use this concept for reidentification in an internal context. For

  reidentification performed by external entities see concept

  UnauthorisedReidentification'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Re-identification
exact_mappings:
- dpv_risk:Reidentification
- dpv_risk_owl:Reidentification
is_a: OperationalSecurityRisk
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Reidentification

```
</details>

### Induced

<details>
```yaml
name: Reidentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Reidentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Re-identification
comments:
- 'Use this concept for reidentification in an internal context. For

  reidentification performed by external entities see concept

  UnauthorisedReidentification'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Re-identification
exact_mappings:
- dpv_risk:Reidentification
- dpv_risk_owl:Reidentification
is_a: OperationalSecurityRisk
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Reidentification

```
</details></div>