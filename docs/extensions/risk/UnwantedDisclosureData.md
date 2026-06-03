---
search:
  boost: 10.0
---

# Class: UnwantedDisclosureData 


_Concept representing Unwanted Disclosure of Data_



<div data-search-exclude markdown="1">



URI: [risk:UnwantedDisclosureData](https://w3id.org/lmodel/dpv/risk/UnwantedDisclosureData)





```mermaid
 classDiagram
    class UnwantedDisclosureData
    click UnwantedDisclosureData href "../UnwantedDisclosureData/"
      ConfidentialityConcept <|-- UnwantedDisclosureData
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- UnwantedDisclosureData
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- UnwantedDisclosureData
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- UnwantedDisclosureData
        click PotentialRiskSource href "../PotentialRiskSource/"
      UnauthorisedActivity <|-- UnwantedDisclosureData
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [UnauthorisedActivity](UnauthorisedActivity.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **UnwantedDisclosureData** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:UnwantedDisclosureData](https://w3id.org/lmodel/dpv/risk/UnwantedDisclosureData) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Unwanted Disclosure of Data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#UnwantedDisclosureData |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:UnwantedDisclosureData |
| native | risk:UnwantedDisclosureData |
| exact | dpv_risk:UnwantedDisclosureData, dpv_risk_owl:UnwantedDisclosureData |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UnwantedDisclosureData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnwantedDisclosureData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unwanted Disclosure of Data
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unwanted Disclosure of Data
exact_mappings:
- dpv_risk:UnwantedDisclosureData
- dpv_risk_owl:UnwantedDisclosureData
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnwantedDisclosureData

```
</details>

### Induced

<details>
```yaml
name: UnwantedDisclosureData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#UnwantedDisclosureData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Unwanted Disclosure of Data
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Unwanted Disclosure of Data
exact_mappings:
- dpv_risk:UnwantedDisclosureData
- dpv_risk_owl:UnwantedDisclosureData
is_a: UnauthorisedActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:UnwantedDisclosureData

```
</details></div>