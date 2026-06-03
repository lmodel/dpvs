---
search:
  boost: 10.0
---

# Class: SecurityQualityInconsistent 


_Concepts representing risks and issues where Quality of Security is_

_Inconsistent_



<div data-search-exclude markdown="1">



URI: [risk:SecurityQualityInconsistent](https://w3id.org/lmodel/dpv/risk/SecurityQualityInconsistent)





```mermaid
 classDiagram
    class SecurityQualityInconsistent
    click SecurityQualityInconsistent href "../SecurityQualityInconsistent/"
      PotentialConsequence <|-- SecurityQualityInconsistent
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SecurityQualityInconsistent
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SecurityQualityInconsistent
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityQualityRisk <|-- SecurityQualityInconsistent
        click SecurityQualityRisk href "../SecurityQualityRisk/"
      QualityInconsistent <|-- SecurityQualityInconsistent
        click QualityInconsistent href "../QualityInconsistent/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityInconsistent](QualityInconsistent.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **SecurityQualityInconsistent** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [SecurityQualityRisk](SecurityQualityRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SecurityQualityInconsistent](https://w3id.org/lmodel/dpv/risk/SecurityQualityInconsistent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Security Quality Inconsistent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SecurityQualityInconsistent |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SecurityQualityInconsistent |
| native | risk:SecurityQualityInconsistent |
| exact | dpv_risk:SecurityQualityInconsistent, dpv_risk_owl:SecurityQualityInconsistent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SecurityQualityInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts representing risks and issues where Quality of Security is

  Inconsistent'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Inconsistent
exact_mappings:
- dpv_risk:SecurityQualityInconsistent
- dpv_risk_owl:SecurityQualityInconsistent
is_a: QualityInconsistent
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- SecurityQualityRisk
class_uri: risk:SecurityQualityInconsistent

```
</details>

### Induced

<details>
```yaml
name: SecurityQualityInconsistent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityInconsistent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts representing risks and issues where Quality of Security is

  Inconsistent'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Inconsistent
exact_mappings:
- dpv_risk:SecurityQualityInconsistent
- dpv_risk_owl:SecurityQualityInconsistent
is_a: QualityInconsistent
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- SecurityQualityRisk
class_uri: risk:SecurityQualityInconsistent

```
</details></div>