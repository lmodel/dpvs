---
search:
  boost: 10.0
---

# Class: UnwantedDataDeletion 


_Concept representing Unwanted Data Deletion_



<div data-search-exclude markdown="1">



URI: [risk:UnwantedDataDeletion](https://w3id.org/lmodel/dpv/risk/UnwantedDataDeletion)





```mermaid
 classDiagram
    class UnwantedDataDeletion
    click UnwantedDataDeletion href "../UnwantedDataDeletion/"
      AvailabilityConcept <|-- UnwantedDataDeletion
        click AvailabilityConcept href "../AvailabilityConcept/"
      IntegrityConcept <|-- UnwantedDataDeletion
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- UnwantedDataDeletion
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnwantedDataDeletion
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnwantedDataDeletion
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnwantedDataDeletion
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnwantedDataDeletion** [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnwantedDataDeletion](https://w3id.org/lmodel/dpv/risk/UnwantedDataDeletion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unwanted Data Deletion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnwantedDataDeletion |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnwantedDataDeletion |
| native | risk:UnwantedDataDeletion |
| exact | dpv_risk:UnwantedDataDeletion, dpv_risk_owl:UnwantedDataDeletion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnwantedDataDeletion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnwantedDataDeletion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unwanted Data Deletion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unwanted Data Deletion
exact_mappings:
- dpv_risk:UnwantedDataDeletion
- dpv_risk_owl:UnwantedDataDeletion
is_a: UnauthorisedActivity
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnwantedDataDeletion

```
</details>

### Induced

<details>
```yaml
name: UnwantedDataDeletion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnwantedDataDeletion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unwanted Data Deletion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unwanted Data Deletion
exact_mappings:
- dpv_risk:UnwantedDataDeletion
- dpv_risk_owl:UnwantedDataDeletion
is_a: UnauthorisedActivity
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnwantedDataDeletion

```
</details></div>