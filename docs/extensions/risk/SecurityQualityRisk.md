---
search:
  boost: 10.0
---

# Class: SecurityQualityRisk 


_Concepts representing risks and issues where Quality of Security is Risk_



<div data-search-exclude markdown="1">



URI: [risk:SecurityQualityRisk](https://w3id.org/lmodel/dpv/risk/SecurityQualityRisk)





```mermaid
 classDiagram
    class SecurityQualityRisk
    click SecurityQualityRisk href "../SecurityQualityRisk/"
      PotentialConsequence <|-- SecurityQualityRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SecurityQualityRisk
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SecurityQualityRisk
        click PotentialRiskSource href "../PotentialRiskSource/"
      QualityRisk <|-- SecurityQualityRisk
        click QualityRisk href "../QualityRisk/"
      

      SecurityQualityRisk <|-- SecurityQualityDegraded
        click SecurityQualityDegraded href "../SecurityQualityDegraded/"
      SecurityQualityRisk <|-- SecurityQualityInconsistent
        click SecurityQualityInconsistent href "../SecurityQualityInconsistent/"
      SecurityQualityRisk <|-- SecurityQualityInsufficient
        click SecurityQualityInsufficient href "../SecurityQualityInsufficient/"
      SecurityQualityRisk <|-- SecurityQualityUnknown
        click SecurityQualityUnknown href "../SecurityQualityUnknown/"
      SecurityQualityRisk <|-- SecurityQualityUnverified
        click SecurityQualityUnverified href "../SecurityQualityUnverified/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **SecurityQualityRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SecurityQualityRisk](https://w3id.org/lmodel/dpv/risk/SecurityQualityRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Security Quality Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SecurityQualityRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SecurityQualityRisk |
| native | risk:SecurityQualityRisk |
| exact | dpv_risk:SecurityQualityRisk, dpv_risk_owl:SecurityQualityRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SecurityQualityRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality of Security is Risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Risk
exact_mappings:
- dpv_risk:SecurityQualityRisk
- dpv_risk_owl:SecurityQualityRisk
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SecurityQualityRisk

```
</details>

### Induced

<details>
```yaml
name: SecurityQualityRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concepts representing risks and issues where Quality of Security is Risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Risk
exact_mappings:
- dpv_risk:SecurityQualityRisk
- dpv_risk_owl:SecurityQualityRisk
is_a: QualityRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SecurityQualityRisk

```
</details></div>