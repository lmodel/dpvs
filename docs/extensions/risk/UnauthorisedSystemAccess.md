---
search:
  boost: 10.0
---

# Class: UnauthorisedSystemAccess 


_Concept representing Unauthorised System Access_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedSystemAccess](https://w3id.org/lmodel/dpv/risk/UnauthorisedSystemAccess)





```mermaid
 classDiagram
    class UnauthorisedSystemAccess
    click UnauthorisedSystemAccess href "../UnauthorisedSystemAccess/"
      ConfidentialityConcept <|-- UnauthorisedSystemAccess
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- UnauthorisedSystemAccess
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- UnauthorisedSystemAccess
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedSystemAccess
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedSystemAccess
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedSystemAccess
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedSystemAccess** [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedSystemAccess](https://w3id.org/lmodel/dpv/risk/UnauthorisedSystemAccess) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised System Access




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedSystemAccess |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedSystemAccess |
| native | risk:UnauthorisedSystemAccess |
| exact | dpv_risk:UnauthorisedSystemAccess, dpv_risk_owl:UnauthorisedSystemAccess |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedSystemAccess
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedSystemAccess
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised System Access
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised System Access
exact_mappings:
- dpv_risk:UnauthorisedSystemAccess
- dpv_risk_owl:UnauthorisedSystemAccess
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedSystemAccess

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedSystemAccess
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedSystemAccess
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised System Access
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised System Access
exact_mappings:
- dpv_risk:UnauthorisedSystemAccess
- dpv_risk_owl:UnauthorisedSystemAccess
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedSystemAccess

```
</details></div>