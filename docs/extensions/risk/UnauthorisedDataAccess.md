---
search:
  boost: 10.0
---

# Class: UnauthorisedDataAccess 


_Concept representing Unauthorised Data Access_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedDataAccess](https://w3id.org/lmodel/dpv/risk/UnauthorisedDataAccess)





```mermaid
 classDiagram
    class UnauthorisedDataAccess
    click UnauthorisedDataAccess href "../UnauthorisedDataAccess/"
      ConfidentialityConcept <|-- UnauthorisedDataAccess
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- UnauthorisedDataAccess
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedDataAccess
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedDataAccess
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedDataAccess
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedDataAccess** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedDataAccess](https://w3id.org/lmodel/dpv/risk/UnauthorisedDataAccess) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised Data Access




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedDataAccess |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedDataAccess |
| native | risk:UnauthorisedDataAccess |
| exact | dpv_risk:UnauthorisedDataAccess, dpv_risk_owl:UnauthorisedDataAccess |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedDataAccess
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedDataAccess
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Data Access
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Data Access
exact_mappings:
- dpv_risk:UnauthorisedDataAccess
- dpv_risk_owl:UnauthorisedDataAccess
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedDataAccess

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedDataAccess
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedDataAccess
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Data Access
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Data Access
exact_mappings:
- dpv_risk:UnauthorisedDataAccess
- dpv_risk_owl:UnauthorisedDataAccess
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedDataAccess

```
</details></div>