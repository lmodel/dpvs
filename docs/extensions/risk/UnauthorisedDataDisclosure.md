---
search:
  boost: 10.0
---

# Class: UnauthorisedDataDisclosure 


_Concept representing Unauthorised Data Disclosure_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedDataDisclosure](https://w3id.org/lmodel/dpv/risk/UnauthorisedDataDisclosure)





```mermaid
 classDiagram
    class UnauthorisedDataDisclosure
    click UnauthorisedDataDisclosure href "../UnauthorisedDataDisclosure/"
      ConfidentialityConcept <|-- UnauthorisedDataDisclosure
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- UnauthorisedDataDisclosure
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedDataDisclosure
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedDataDisclosure
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedDataDisclosure
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedDataDisclosure** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedDataDisclosure](https://w3id.org/lmodel/dpv/risk/UnauthorisedDataDisclosure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised Data Disclosure




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedDataDisclosure |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedDataDisclosure |
| native | risk:UnauthorisedDataDisclosure |
| exact | dpv_risk:UnauthorisedDataDisclosure, dpv_risk_owl:UnauthorisedDataDisclosure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedDataDisclosure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedDataDisclosure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Data Disclosure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Data Disclosure
exact_mappings:
- dpv_risk:UnauthorisedDataDisclosure
- dpv_risk_owl:UnauthorisedDataDisclosure
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedDataDisclosure

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedDataDisclosure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedDataDisclosure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Data Disclosure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Data Disclosure
exact_mappings:
- dpv_risk:UnauthorisedDataDisclosure
- dpv_risk_owl:UnauthorisedDataDisclosure
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedDataDisclosure

```
</details></div>