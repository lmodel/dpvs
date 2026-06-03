---
search:
  boost: 10.0
---

# Class: SecurityQualityUnknown 


_Concepts representing risks and issues where Quality of Security is_

_Unknown_



<div data-search-exclude markdown="1">



URI: [risk:SecurityQualityUnknown](https://w3id.org/lmodel/dpv/risk/SecurityQualityUnknown)





```mermaid
 classDiagram
    class SecurityQualityUnknown
    click SecurityQualityUnknown href "../SecurityQualityUnknown/"
      PotentialConsequence <|-- SecurityQualityUnknown
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SecurityQualityUnknown
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SecurityQualityUnknown
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityQualityRisk <|-- SecurityQualityUnknown
        click SecurityQualityRisk href "../SecurityQualityRisk/"
      QualityUnknown <|-- SecurityQualityUnknown
        click QualityUnknown href "../QualityUnknown/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [QualityRisk](QualityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [QualityUnknown](QualityUnknown.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **SecurityQualityUnknown** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [SecurityQualityRisk](SecurityQualityRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SecurityQualityUnknown](https://w3id.org/lmodel/dpv/risk/SecurityQualityUnknown) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Security Quality Unknown




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#SecurityQualityUnknown |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SecurityQualityUnknown |
| native | risk:SecurityQualityUnknown |
| exact | dpv_risk:SecurityQualityUnknown, dpv_risk_owl:SecurityQualityUnknown |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SecurityQualityUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts representing risks and issues where Quality of Security is

  Unknown'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Unknown
exact_mappings:
- dpv_risk:SecurityQualityUnknown
- dpv_risk_owl:SecurityQualityUnknown
is_a: QualityUnknown
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- SecurityQualityRisk
class_uri: risk:SecurityQualityUnknown

```
</details>

### Induced

<details>
```yaml
name: SecurityQualityUnknown
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SecurityQualityUnknown
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concepts representing risks and issues where Quality of Security is

  Unknown'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Security Quality Unknown
exact_mappings:
- dpv_risk:SecurityQualityUnknown
- dpv_risk_owl:SecurityQualityUnknown
is_a: QualityUnknown
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- SecurityQualityRisk
class_uri: risk:SecurityQualityUnknown

```
</details></div>