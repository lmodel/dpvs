---
search:
  boost: 10.0
---

# Class: IntegrityBreach 


_Concept representing a breach of integrity_



<div data-search-exclude markdown="1">



URI: [risk:IntegrityBreach](https://w3id.org/lmodel/dpv/risk/IntegrityBreach)





```mermaid
 classDiagram
    class IntegrityBreach
    click IntegrityBreach href "../IntegrityBreach/"
      IntegrityConcept <|-- IntegrityBreach
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- IntegrityBreach
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- IntegrityBreach
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- IntegrityBreach
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataBreach <|-- IntegrityBreach
        click DataBreach href "../DataBreach/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityBreach](SecurityBreach.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataBreach](DataBreach.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **IntegrityBreach** [ [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IntegrityBreach](https://w3id.org/lmodel/dpv/risk/IntegrityBreach) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Integrity Breach




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IntegrityBreach |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IntegrityBreach |
| native | risk:IntegrityBreach |
| exact | dpv_risk:IntegrityBreach, dpv_risk_owl:IntegrityBreach |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntegrityBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IntegrityBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing a breach of integrity
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Integrity Breach
exact_mappings:
- dpv_risk:IntegrityBreach
- dpv_risk_owl:IntegrityBreach
is_a: DataBreach
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IntegrityBreach

```
</details>

### Induced

<details>
```yaml
name: IntegrityBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IntegrityBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing a breach of integrity
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Integrity Breach
exact_mappings:
- dpv_risk:IntegrityBreach
- dpv_risk_owl:IntegrityBreach
is_a: DataBreach
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IntegrityBreach

```
</details></div>