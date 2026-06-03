---
search:
  boost: 10.0
---

# Class: AvailabilityBreach 


_Concept representing a breach of availability_



<div data-search-exclude markdown="1">



URI: [risk:AvailabilityBreach](https://w3id.org/lmodel/dpv/risk/AvailabilityBreach)





```mermaid
 classDiagram
    class AvailabilityBreach
    click AvailabilityBreach href "../AvailabilityBreach/"
      AvailabilityConcept <|-- AvailabilityBreach
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialConsequence <|-- AvailabilityBreach
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- AvailabilityBreach
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- AvailabilityBreach
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataBreach <|-- AvailabilityBreach
        click DataBreach href "../DataBreach/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityBreach](SecurityBreach.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataBreach](DataBreach.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **AvailabilityBreach** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:AvailabilityBreach](https://w3id.org/lmodel/dpv/risk/AvailabilityBreach) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Availability Breach




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#AvailabilityBreach |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:AvailabilityBreach |
| native | risk:AvailabilityBreach |
| exact | dpv_risk:AvailabilityBreach, dpv_risk_owl:AvailabilityBreach |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AvailabilityBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvailabilityBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing a breach of availability
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Availability Breach
exact_mappings:
- dpv_risk:AvailabilityBreach
- dpv_risk_owl:AvailabilityBreach
is_a: DataBreach
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:AvailabilityBreach

```
</details>

### Induced

<details>
```yaml
name: AvailabilityBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#AvailabilityBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing a breach of availability
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Availability Breach
exact_mappings:
- dpv_risk:AvailabilityBreach
- dpv_risk_owl:AvailabilityBreach
is_a: DataBreach
mixins:
- AvailabilityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:AvailabilityBreach

```
</details></div>