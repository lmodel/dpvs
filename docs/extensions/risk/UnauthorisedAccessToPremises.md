---
search:
  boost: 10.0
---

# Class: UnauthorisedAccessToPremises 


_Concept representing Unauthorised Access to Premises_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedAccessToPremises](https://w3id.org/lmodel/dpv/risk/UnauthorisedAccessToPremises)





```mermaid
 classDiagram
    class UnauthorisedAccessToPremises
    click UnauthorisedAccessToPremises href "../UnauthorisedAccessToPremises/"
      AvailabilityConcept <|-- UnauthorisedAccessToPremises
        click AvailabilityConcept href "../AvailabilityConcept/"
      ConfidentialityConcept <|-- UnauthorisedAccessToPremises
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- UnauthorisedAccessToPremises
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- UnauthorisedAccessToPremises
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedAccessToPremises
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedAccessToPremises
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedAccessToPremises
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedAccessToPremises** [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedAccessToPremises](https://w3id.org/lmodel/dpv/risk/UnauthorisedAccessToPremises) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised Access to Premises




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedAccessToPremises |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedAccessToPremises |
| native | risk:UnauthorisedAccessToPremises |
| exact | dpv_risk:UnauthorisedAccessToPremises, dpv_risk_owl:UnauthorisedAccessToPremises |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedAccessToPremises
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedAccessToPremises
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Access to Premises
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Access to Premises
exact_mappings:
- dpv_risk:UnauthorisedAccessToPremises
- dpv_risk_owl:UnauthorisedAccessToPremises
is_a: UnauthorisedActivity
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedAccessToPremises

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedAccessToPremises
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedAccessToPremises
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Access to Premises
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Access to Premises
exact_mappings:
- dpv_risk:UnauthorisedAccessToPremises
- dpv_risk_owl:UnauthorisedAccessToPremises
is_a: UnauthorisedActivity
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedAccessToPremises

```
</details></div>