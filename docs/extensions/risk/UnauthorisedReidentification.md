---
search:
  boost: 10.0
---

# Class: UnauthorisedReidentification 


_Concept representing Unauthorised Re-Identification_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedReidentification](https://w3id.org/lmodel/dpv/risk/UnauthorisedReidentification)





```mermaid
 classDiagram
    class UnauthorisedReidentification
    click UnauthorisedReidentification href "../UnauthorisedReidentification/"
      ConfidentialityConcept <|-- UnauthorisedReidentification
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- UnauthorisedReidentification
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedReidentification
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedReidentification
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedReidentification
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedReidentification** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedReidentification](https://w3id.org/lmodel/dpv/risk/UnauthorisedReidentification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised Re-Identification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedReidentification |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedReidentification |
| native | risk:UnauthorisedReidentification |
| exact | dpv_risk:UnauthorisedReidentification, dpv_risk_owl:UnauthorisedReidentification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedReidentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedReidentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Re-Identification
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Re-Identification
exact_mappings:
- dpv_risk:UnauthorisedReidentification
- dpv_risk_owl:UnauthorisedReidentification
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedReidentification

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedReidentification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedReidentification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Re-Identification
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Re-Identification
exact_mappings:
- dpv_risk:UnauthorisedReidentification
- dpv_risk_owl:UnauthorisedReidentification
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedReidentification

```
</details></div>