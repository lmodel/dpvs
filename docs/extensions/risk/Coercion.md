---
search:
  boost: 10.0
---

# Class: Coercion 


_Concept representing Coercion_



<div data-search-exclude markdown="1">



URI: [risk:Coercion](https://w3id.org/lmodel/dpv/risk/Coercion)





```mermaid
 classDiagram
    class Coercion
    click Coercion href "../Coercion/"
      ConfidentialityConcept <|-- Coercion
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- Coercion
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Coercion
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Coercion
        click PotentialRiskSource href "../PotentialRiskSource/"
      Exploitation <|-- Coercion
        click Exploitation href "../Exploitation/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [Exploitation](Exploitation.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **Coercion** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Coercion](https://w3id.org/lmodel/dpv/risk/Coercion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Coercion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Coercion |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Coercion |
| native | risk:Coercion |
| exact | dpv_risk:Coercion, dpv_risk_owl:Coercion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Coercion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Coercion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Coercion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Coercion
exact_mappings:
- dpv_risk:Coercion
- dpv_risk_owl:Coercion
is_a: Exploitation
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Coercion

```
</details>

### Induced

<details>
```yaml
name: Coercion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Coercion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Coercion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Coercion
exact_mappings:
- dpv_risk:Coercion
- dpv_risk_owl:Coercion
is_a: Exploitation
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Coercion

```
</details></div>