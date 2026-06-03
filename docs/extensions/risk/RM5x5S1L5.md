---
search:
  boost: 10.0
---

# Class: RM5x5S1L5 


_Node in a 5x5 Risk Matrix with Risk Severity: Very Low; Likelihood: Very_

_High; and Risk Level: Low_



<div data-search-exclude markdown="1">



URI: [risk:RM5x5S1L5](https://w3id.org/lmodel/dpv/risk/RM5x5S1L5)





```mermaid
 classDiagram
    class RM5x5S1L5
    click RM5x5S1L5 href "../RM5x5S1L5/"
      RiskAnalysis <|-- RM5x5S1L5
        click RiskAnalysis href "../RiskAnalysis/"
      RiskMatrix5x5 <|-- RM5x5S1L5
        click RiskMatrix5x5 href "../RiskMatrix5x5/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * [RiskAnalysis](RiskAnalysis.md)
            * [RiskMatrix](RiskMatrix.md)
                * [RiskMatrix5x5](RiskMatrix5x5.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * **RM5x5S1L5** [ [RiskAnalysis](RiskAnalysis.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RM5x5S1L5](https://w3id.org/lmodel/dpv/risk/RM5x5S1L5) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Low Risk (RM5x5 S:1 L:5)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RM5x5S1L5 |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RM5x5S1L5 |
| native | risk:RM5x5S1L5 |
| exact | dpv_risk:RM5x5S1L5, dpv_risk_owl:RM5x5S1L5 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RM5x5S1L5
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM5x5S1L5
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 5x5 Risk Matrix with Risk Severity: Very Low; Likelihood:
  Very

  High; and Risk Level: Low'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Low Risk (RM5x5 S:1 L:5)
exact_mappings:
- dpv_risk:RM5x5S1L5
- dpv_risk_owl:RM5x5S1L5
is_a: RiskMatrix5x5
mixins:
- RiskAnalysis
class_uri: risk:RM5x5S1L5

```
</details>

### Induced

<details>
```yaml
name: RM5x5S1L5
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM5x5S1L5
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 5x5 Risk Matrix with Risk Severity: Very Low; Likelihood:
  Very

  High; and Risk Level: Low'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Low Risk (RM5x5 S:1 L:5)
exact_mappings:
- dpv_risk:RM5x5S1L5
- dpv_risk_owl:RM5x5S1L5
is_a: RiskMatrix5x5
mixins:
- RiskAnalysis
class_uri: risk:RM5x5S1L5

```
</details></div>