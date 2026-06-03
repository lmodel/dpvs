---
search:
  boost: 10.0
---

# Class: RM3x3S2L3 


_Node in a 3x3 Risk Matrix with Risk Severity: Moderate; Likelihood:_

_High; and Risk Level: High_



<div data-search-exclude markdown="1">



URI: [risk:RM3x3S2L3](https://w3id.org/lmodel/dpv/risk/RM3x3S2L3)





```mermaid
 classDiagram
    class RM3x3S2L3
    click RM3x3S2L3 href "../RM3x3S2L3/"
      RiskAnalysis <|-- RM3x3S2L3
        click RiskAnalysis href "../RiskAnalysis/"
      RiskMatrix3x3 <|-- RM3x3S2L3
        click RiskMatrix3x3 href "../RiskMatrix3x3/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * [RiskAnalysis](RiskAnalysis.md)
            * [RiskMatrix](RiskMatrix.md)
                * [RiskMatrix3x3](RiskMatrix3x3.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * **RM3x3S2L3** [ [RiskAnalysis](RiskAnalysis.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RM3x3S2L3](https://w3id.org/lmodel/dpv/risk/RM3x3S2L3) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* High Risk (RM3x3 S:2 L:3)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RM3x3S2L3 |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RM3x3S2L3 |
| native | risk:RM3x3S2L3 |
| exact | dpv_risk:RM3x3S2L3, dpv_risk_owl:RM3x3S2L3 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RM3x3S2L3
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM3x3S2L3
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 3x3 Risk Matrix with Risk Severity: Moderate; Likelihood:

  High; and Risk Level: High'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- High Risk (RM3x3 S:2 L:3)
exact_mappings:
- dpv_risk:RM3x3S2L3
- dpv_risk_owl:RM3x3S2L3
is_a: RiskMatrix3x3
mixins:
- RiskAnalysis
class_uri: risk:RM3x3S2L3

```
</details>

### Induced

<details>
```yaml
name: RM3x3S2L3
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM3x3S2L3
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 3x3 Risk Matrix with Risk Severity: Moderate; Likelihood:

  High; and Risk Level: High'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- High Risk (RM3x3 S:2 L:3)
exact_mappings:
- dpv_risk:RM3x3S2L3
- dpv_risk_owl:RM3x3S2L3
is_a: RiskMatrix3x3
mixins:
- RiskAnalysis
class_uri: risk:RM3x3S2L3

```
</details></div>