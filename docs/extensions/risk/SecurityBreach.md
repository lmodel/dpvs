---
search:
  boost: 10.0
---

# Class: SecurityBreach 


_Concept representing Security Breach_



<div data-search-exclude markdown="1">



URI: [risk:SecurityBreach](https://w3id.org/lmodel/dpv/risk/SecurityBreach)





```mermaid
 classDiagram
    class SecurityBreach
    click SecurityBreach href "../SecurityBreach/"
      AvailabilityConcept <|-- SecurityBreach
        click AvailabilityConcept href "../AvailabilityConcept/"
      ConfidentialityConcept <|-- SecurityBreach
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- SecurityBreach
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- SecurityBreach
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SecurityBreach
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SecurityBreach
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- SecurityBreach
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      

      SecurityBreach <|-- DataBreach
        click DataBreach href "../DataBreach/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **SecurityBreach** [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataBreach](DataBreach.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SecurityBreach](https://w3id.org/lmodel/dpv/risk/SecurityBreach) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Security Breach




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SecurityBreach |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SecurityBreach |
| native | risk:SecurityBreach |
| exact | dpv_risk:SecurityBreach, dpv_risk_owl:SecurityBreach |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SecurityBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Security Breach
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Breach
exact_mappings:
- dpv_risk:SecurityBreach
- dpv_risk_owl:SecurityBreach
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SecurityBreach

```
</details>

### Induced

<details>
```yaml
name: SecurityBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Security Breach
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Breach
exact_mappings:
- dpv_risk:SecurityBreach
- dpv_risk_owl:SecurityBreach
is_a: OperationalSecurityRisk
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SecurityBreach

```
</details></div>