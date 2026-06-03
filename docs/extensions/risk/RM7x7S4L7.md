---
search:
  boost: 10.0
---

# Class: RM7x7S4L7 


_Node in a 7x7 Risk Matrix with Risk Severity: Moderate; Likelihood:_

_Extremely High; and Risk Level: Very High_



<div data-search-exclude markdown="1">



URI: [risk:RM7x7S4L7](https://w3id.org/lmodel/dpv/risk/RM7x7S4L7)





```mermaid
 classDiagram
    class RM7x7S4L7
    click RM7x7S4L7 href "../RM7x7S4L7/"
      RiskAnalysis <|-- RM7x7S4L7
        click RiskAnalysis href "../RiskAnalysis/"
      RiskMatrix7x7 <|-- RM7x7S4L7
        click RiskMatrix7x7 href "../RiskMatrix7x7/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * [RiskAnalysis](RiskAnalysis.md)
            * [RiskMatrix](RiskMatrix.md)
                * [RiskMatrix7x7](RiskMatrix7x7.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * **RM7x7S4L7** [ [RiskAnalysis](RiskAnalysis.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RM7x7S4L7](https://w3id.org/lmodel/dpv/risk/RM7x7S4L7) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Very High Risk (RM7x7 S:4 L:7)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RM7x7S4L7 |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RM7x7S4L7 |
| native | risk:RM7x7S4L7 |
| exact | dpv_risk:RM7x7S4L7, dpv_risk_owl:RM7x7S4L7 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RM7x7S4L7
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM7x7S4L7
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 7x7 Risk Matrix with Risk Severity: Moderate; Likelihood:

  Extremely High; and Risk Level: Very High'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very High Risk (RM7x7 S:4 L:7)
exact_mappings:
- dpv_risk:RM7x7S4L7
- dpv_risk_owl:RM7x7S4L7
is_a: RiskMatrix7x7
mixins:
- RiskAnalysis
class_uri: risk:RM7x7S4L7

```
</details>

### Induced

<details>
```yaml
name: RM7x7S4L7
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM7x7S4L7
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 7x7 Risk Matrix with Risk Severity: Moderate; Likelihood:

  Extremely High; and Risk Level: Very High'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very High Risk (RM7x7 S:4 L:7)
exact_mappings:
- dpv_risk:RM7x7S4L7
- dpv_risk_owl:RM7x7S4L7
is_a: RiskMatrix7x7
mixins:
- RiskAnalysis
class_uri: risk:RM7x7S4L7

```
</details></div>