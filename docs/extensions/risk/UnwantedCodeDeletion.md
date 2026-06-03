---
search:
  boost: 10.0
---

# Class: UnwantedCodeDeletion 


_Concept representing Unwanted Code Deletion_



<div data-search-exclude markdown="1">



URI: [risk:UnwantedCodeDeletion](https://w3id.org/lmodel/dpv/risk/UnwantedCodeDeletion)





```mermaid
 classDiagram
    class UnwantedCodeDeletion
    click UnwantedCodeDeletion href "../UnwantedCodeDeletion/"
      AvailabilityConcept <|-- UnwantedCodeDeletion
        click AvailabilityConcept href "../AvailabilityConcept/"
      IntegrityConcept <|-- UnwantedCodeDeletion
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- UnwantedCodeDeletion
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnwantedCodeDeletion
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnwantedCodeDeletion
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnwantedCodeDeletion
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnwantedCodeDeletion** [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnwantedCodeDeletion](https://w3id.org/lmodel/dpv/risk/UnwantedCodeDeletion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unwanted Code Deletion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnwantedCodeDeletion |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnwantedCodeDeletion |
| native | risk:UnwantedCodeDeletion |
| exact | dpv_risk:UnwantedCodeDeletion, dpv_risk_owl:UnwantedCodeDeletion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnwantedCodeDeletion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnwantedCodeDeletion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unwanted Code Deletion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unwanted Code Deletion
exact_mappings:
- dpv_risk:UnwantedCodeDeletion
- dpv_risk_owl:UnwantedCodeDeletion
is_a: UnauthorisedActivity
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnwantedCodeDeletion

```
</details>

### Induced

<details>
```yaml
name: UnwantedCodeDeletion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnwantedCodeDeletion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unwanted Code Deletion
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unwanted Code Deletion
exact_mappings:
- dpv_risk:UnwantedCodeDeletion
- dpv_risk_owl:UnwantedCodeDeletion
is_a: UnauthorisedActivity
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnwantedCodeDeletion

```
</details></div>