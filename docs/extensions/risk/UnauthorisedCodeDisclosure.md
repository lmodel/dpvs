---
search:
  boost: 10.0
---

# Class: UnauthorisedCodeDisclosure 


_Concept representing Unauthorised Code Disclosure_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedCodeDisclosure](https://w3id.org/lmodel/dpv/risk/UnauthorisedCodeDisclosure)





```mermaid
 classDiagram
    class UnauthorisedCodeDisclosure
    click UnauthorisedCodeDisclosure href "../UnauthorisedCodeDisclosure/"
      ConfidentialityConcept <|-- UnauthorisedCodeDisclosure
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- UnauthorisedCodeDisclosure
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedCodeDisclosure
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedCodeDisclosure
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedCodeDisclosure
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedCodeDisclosure** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedCodeDisclosure](https://w3id.org/lmodel/dpv/risk/UnauthorisedCodeDisclosure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised Code Disclosure




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedCodeDisclosure |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedCodeDisclosure |
| native | risk:UnauthorisedCodeDisclosure |
| exact | dpv_risk:UnauthorisedCodeDisclosure, dpv_risk_owl:UnauthorisedCodeDisclosure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedCodeDisclosure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedCodeDisclosure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Code Disclosure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Code Disclosure
exact_mappings:
- dpv_risk:UnauthorisedCodeDisclosure
- dpv_risk_owl:UnauthorisedCodeDisclosure
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedCodeDisclosure

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedCodeDisclosure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedCodeDisclosure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Code Disclosure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Code Disclosure
exact_mappings:
- dpv_risk:UnauthorisedCodeDisclosure
- dpv_risk_owl:UnauthorisedCodeDisclosure
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedCodeDisclosure

```
</details></div>