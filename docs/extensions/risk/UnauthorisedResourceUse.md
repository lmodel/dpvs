---
search:
  boost: 10.0
---

# Class: UnauthorisedResourceUse 


_Concept representing Unauthorised Resource Use_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedResourceUse](https://w3id.org/lmodel/dpv/risk/UnauthorisedResourceUse)





```mermaid
 classDiagram
    class UnauthorisedResourceUse
    click UnauthorisedResourceUse href "../UnauthorisedResourceUse/"
      AvailabilityConcept <|-- UnauthorisedResourceUse
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialConsequence <|-- UnauthorisedResourceUse
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedResourceUse
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedResourceUse
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedResourceUse
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedResourceUse** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedResourceUse](https://w3id.org/lmodel/dpv/risk/UnauthorisedResourceUse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised Resource Use




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedResourceUse |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedResourceUse |
| native | risk:UnauthorisedResourceUse |
| exact | dpv_risk:UnauthorisedResourceUse, dpv_risk_owl:UnauthorisedResourceUse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedResourceUse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedResourceUse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Resource Use
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Resource Use
exact_mappings:
- dpv_risk:UnauthorisedResourceUse
- dpv_risk_owl:UnauthorisedResourceUse
is_a: UnauthorisedActivity
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedResourceUse

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedResourceUse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedResourceUse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Resource Use
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Resource Use
exact_mappings:
- dpv_risk:UnauthorisedResourceUse
- dpv_risk_owl:UnauthorisedResourceUse
is_a: UnauthorisedActivity
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedResourceUse

```
</details></div>