---
search:
  boost: 10.0
---

# Class: UnauthorisedSystemModification 


_Concept representing Unauthorised System Modification_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedSystemModification](https://w3id.org/lmodel/dpv/risk/UnauthorisedSystemModification)





```mermaid
 classDiagram
    class UnauthorisedSystemModification
    click UnauthorisedSystemModification href "../UnauthorisedSystemModification/"
      IntegrityConcept <|-- UnauthorisedSystemModification
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- UnauthorisedSystemModification
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedSystemModification
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedSystemModification
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedSystemModification
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedSystemModification** [ [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedSystemModification](https://w3id.org/lmodel/dpv/risk/UnauthorisedSystemModification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised System Modification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedSystemModification |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedSystemModification |
| native | risk:UnauthorisedSystemModification |
| exact | dpv_risk:UnauthorisedSystemModification, dpv_risk_owl:UnauthorisedSystemModification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedSystemModification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedSystemModification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised System Modification
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised System Modification
exact_mappings:
- dpv_risk:UnauthorisedSystemModification
- dpv_risk_owl:UnauthorisedSystemModification
is_a: UnauthorisedActivity
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedSystemModification

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedSystemModification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedSystemModification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised System Modification
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised System Modification
exact_mappings:
- dpv_risk:UnauthorisedSystemModification
- dpv_risk_owl:UnauthorisedSystemModification
is_a: UnauthorisedActivity
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedSystemModification

```
</details></div>