---
search:
  boost: 10.0
---

# Class: UnauthorisedCodeAccess 


_Concept representing Unauthorised Code Access_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedCodeAccess](https://w3id.org/lmodel/dpv/risk/UnauthorisedCodeAccess)





```mermaid
 classDiagram
    class UnauthorisedCodeAccess
    click UnauthorisedCodeAccess href "../UnauthorisedCodeAccess/"
      ConfidentialityConcept <|-- UnauthorisedCodeAccess
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- UnauthorisedCodeAccess
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- UnauthorisedCodeAccess
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedCodeAccess
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedCodeAccess
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedCodeAccess
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedCodeAccess** [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedCodeAccess](https://w3id.org/lmodel/dpv/risk/UnauthorisedCodeAccess) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised Code Access




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedCodeAccess |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedCodeAccess |
| native | risk:UnauthorisedCodeAccess |
| exact | dpv_risk:UnauthorisedCodeAccess, dpv_risk_owl:UnauthorisedCodeAccess |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedCodeAccess
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedCodeAccess
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Code Access
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Code Access
exact_mappings:
- dpv_risk:UnauthorisedCodeAccess
- dpv_risk_owl:UnauthorisedCodeAccess
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedCodeAccess

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedCodeAccess
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedCodeAccess
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Code Access
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Code Access
exact_mappings:
- dpv_risk:UnauthorisedCodeAccess
- dpv_risk_owl:UnauthorisedCodeAccess
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedCodeAccess

```
</details></div>