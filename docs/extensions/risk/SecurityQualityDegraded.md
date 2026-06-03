---
search:
  boost: 10.0
---

# Class: SecurityQualityDegraded 


_Concepts representing risks and issues where Quality of Security is_

_Degraded_



<div data-search-exclude markdown="1">



URI: [risk:SecurityQualityDegraded](https://w3id.org/lmodel/dpv/risk/SecurityQualityDegraded)





```mermaid
 classDiagram
    class SecurityQualityDegraded
    click SecurityQualityDegraded href "../SecurityQualityDegraded/"
      PotentialConsequence <|-- SecurityQualityDegraded
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SecurityQualityDegraded
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SecurityQualityDegraded
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityQualityRisk <|-- SecurityQualityDegraded
        click SecurityQualityRisk href "../SecurityQualityRisk/"
      QualityDegraded <|-- SecurityQualityDegraded
        click QualityDegraded href "../QualityDegraded/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityDegraded](QualityDegraded.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **SecurityQualityDegraded** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [SecurityQualityRisk](SecurityQualityRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SecurityQualityDegraded](https://w3id.org/lmodel/dpv/risk/SecurityQualityDegraded) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Security Quality Degraded




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SecurityQualityDegraded |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SecurityQualityDegraded |
| native | risk:SecurityQualityDegraded |
| exact | dpv_risk:SecurityQualityDegraded, dpv_risk_owl:SecurityQualityDegraded |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SecurityQualityDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts representing risks and issues where Quality of Security is

  Degraded'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Degraded
exact_mappings:
- dpv_risk:SecurityQualityDegraded
- dpv_risk_owl:SecurityQualityDegraded
is_a: QualityDegraded
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- SecurityQualityRisk
class_uri: risk:SecurityQualityDegraded

```
</details>

### Induced

<details>
```yaml
name: SecurityQualityDegraded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityDegraded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts representing risks and issues where Quality of Security is

  Degraded'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Degraded
exact_mappings:
- dpv_risk:SecurityQualityDegraded
- dpv_risk_owl:SecurityQualityDegraded
is_a: QualityDegraded
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- SecurityQualityRisk
class_uri: risk:SecurityQualityDegraded

```
</details></div>