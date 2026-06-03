---
search:
  boost: 10.0
---

# Class: DataBreach 


_Concept representing Data Breach_



<div data-search-exclude markdown="1">



URI: [risk:DataBreach](https://w3id.org/lmodel/dpv/risk/DataBreach)





```mermaid
 classDiagram
    class DataBreach
    click DataBreach href "../DataBreach/"
      AvailabilityConcept <|-- DataBreach
        click AvailabilityConcept href "../AvailabilityConcept/"
      ConfidentialityConcept <|-- DataBreach
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- DataBreach
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- DataBreach
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataBreach
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataBreach
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityBreach <|-- DataBreach
        click SecurityBreach href "../SecurityBreach/"
      

      DataBreach <|-- AvailabilityBreach
        click AvailabilityBreach href "../AvailabilityBreach/"
      DataBreach <|-- ConfidentialityBreach
        click ConfidentialityBreach href "../ConfidentialityBreach/"
      DataBreach <|-- IntegrityBreach
        click IntegrityBreach href "../IntegrityBreach/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityBreach](SecurityBreach.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **DataBreach** [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [AvailabilityBreach](AvailabilityBreach.md) [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [ConfidentialityBreach](ConfidentialityBreach.md) [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [IntegrityBreach](IntegrityBreach.md) [ [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataBreach](https://w3id.org/lmodel/dpv/risk/DataBreach) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Breach




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataBreach |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataBreach |
| native | risk:DataBreach |
| exact | dpv_risk:DataBreach, dpv_risk_owl:DataBreach |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Data Breach
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Breach
exact_mappings:
- dpv_risk:DataBreach
- dpv_risk_owl:DataBreach
is_a: SecurityBreach
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataBreach

```
</details>

### Induced

<details>
```yaml
name: DataBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Data Breach
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Breach
exact_mappings:
- dpv_risk:DataBreach
- dpv_risk_owl:DataBreach
is_a: SecurityBreach
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataBreach

```
</details></div>