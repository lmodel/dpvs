---
search:
  boost: 10.0
---

# Class: SecurityQualityInsufficient 


_Concepts representing risks and issues where Quality of Security is_

_Insufficient_



<div data-search-exclude markdown="1">



URI: [risk:SecurityQualityInsufficient](https://w3id.org/lmodel/dpv/risk/SecurityQualityInsufficient)





```mermaid
 classDiagram
    class SecurityQualityInsufficient
    click SecurityQualityInsufficient href "../SecurityQualityInsufficient/"
      PotentialConsequence <|-- SecurityQualityInsufficient
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SecurityQualityInsufficient
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SecurityQualityInsufficient
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityQualityRisk <|-- SecurityQualityInsufficient
        click SecurityQualityRisk href "../SecurityQualityRisk/"
      QualityInsufficient <|-- SecurityQualityInsufficient
        click QualityInsufficient href "../QualityInsufficient/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityInsufficient](QualityInsufficient.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **SecurityQualityInsufficient** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [SecurityQualityRisk](SecurityQualityRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SecurityQualityInsufficient](https://w3id.org/lmodel/dpv/risk/SecurityQualityInsufficient) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Security Quality Insufficient




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SecurityQualityInsufficient |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SecurityQualityInsufficient |
| native | risk:SecurityQualityInsufficient |
| exact | dpv_risk:SecurityQualityInsufficient, dpv_risk_owl:SecurityQualityInsufficient |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SecurityQualityInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts representing risks and issues where Quality of Security is

  Insufficient'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Insufficient
exact_mappings:
- dpv_risk:SecurityQualityInsufficient
- dpv_risk_owl:SecurityQualityInsufficient
is_a: QualityInsufficient
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- SecurityQualityRisk
class_uri: risk:SecurityQualityInsufficient

```
</details>

### Induced

<details>
```yaml
name: SecurityQualityInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts representing risks and issues where Quality of Security is

  Insufficient'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Insufficient
exact_mappings:
- dpv_risk:SecurityQualityInsufficient
- dpv_risk_owl:SecurityQualityInsufficient
is_a: QualityInsufficient
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- SecurityQualityRisk
class_uri: risk:SecurityQualityInsufficient

```
</details></div>