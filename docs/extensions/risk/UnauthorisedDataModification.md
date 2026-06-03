---
search:
  boost: 10.0
---

# Class: UnauthorisedDataModification 


_Concept representing Unauthorised Data Modification_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedDataModification](https://w3id.org/lmodel/dpv/risk/UnauthorisedDataModification)





```mermaid
 classDiagram
    class UnauthorisedDataModification
    click UnauthorisedDataModification href "../UnauthorisedDataModification/"
      IntegrityConcept <|-- UnauthorisedDataModification
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- UnauthorisedDataModification
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedDataModification
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedDataModification
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedDataModification
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedDataModification** [ [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedDataModification](https://w3id.org/lmodel/dpv/risk/UnauthorisedDataModification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised Data Modification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedDataModification |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedDataModification |
| native | risk:UnauthorisedDataModification |
| exact | dpv_risk:UnauthorisedDataModification, dpv_risk_owl:UnauthorisedDataModification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedDataModification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedDataModification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Data Modification
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Data Modification
exact_mappings:
- dpv_risk:UnauthorisedDataModification
- dpv_risk_owl:UnauthorisedDataModification
is_a: UnauthorisedActivity
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedDataModification

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedDataModification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedDataModification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Data Modification
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Data Modification
exact_mappings:
- dpv_risk:UnauthorisedDataModification
- dpv_risk_owl:UnauthorisedDataModification
is_a: UnauthorisedActivity
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedDataModification

```
</details></div>