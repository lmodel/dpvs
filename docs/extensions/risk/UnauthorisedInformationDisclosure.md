---
search:
  boost: 10.0
---

# Class: UnauthorisedInformationDisclosure 


_Concept representing Unauthorised Information Disclosure_



<div data-search-exclude markdown="1">



URI: [risk:UnauthorisedInformationDisclosure](https://w3id.org/lmodel/dpv/risk/UnauthorisedInformationDisclosure)





```mermaid
 classDiagram
    class UnauthorisedInformationDisclosure
    click UnauthorisedInformationDisclosure href "../UnauthorisedInformationDisclosure/"
      ConfidentialityConcept <|-- UnauthorisedInformationDisclosure
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- UnauthorisedInformationDisclosure
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnauthorisedInformationDisclosure
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnauthorisedInformationDisclosure
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnauthorisedInformationDisclosure
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnauthorisedInformationDisclosure** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnauthorisedInformationDisclosure](https://w3id.org/lmodel/dpv/risk/UnauthorisedInformationDisclosure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unauthorised Information Disclosure




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnauthorisedInformationDisclosure |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnauthorisedInformationDisclosure |
| native | risk:UnauthorisedInformationDisclosure |
| exact | dpv_risk:UnauthorisedInformationDisclosure, dpv_risk_owl:UnauthorisedInformationDisclosure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnauthorisedInformationDisclosure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedInformationDisclosure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Information Disclosure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Information Disclosure
exact_mappings:
- dpv_risk:UnauthorisedInformationDisclosure
- dpv_risk_owl:UnauthorisedInformationDisclosure
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedInformationDisclosure

```
</details>

### Induced

<details>
```yaml
name: UnauthorisedInformationDisclosure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnauthorisedInformationDisclosure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unauthorised Information Disclosure
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unauthorised Information Disclosure
exact_mappings:
- dpv_risk:UnauthorisedInformationDisclosure
- dpv_risk_owl:UnauthorisedInformationDisclosure
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnauthorisedInformationDisclosure

```
</details></div>