---
search:
  boost: 10.0
---

# Class: RM3x3S2L1 


_Node in a 3x3 Risk Matrix with Risk Severity: Moderate; Likelihood: Low;_

_and Risk Level: Low_



<div data-search-exclude markdown="1">



URI: [risk:RM3x3S2L1](https://w3id.org/lmodel/dpv/risk/RM3x3S2L1)





```mermaid
 classDiagram
    class RM3x3S2L1
    click RM3x3S2L1 href "../RM3x3S2L1/"
      RiskAnalysis <|-- RM3x3S2L1
        click RiskAnalysis href "../RiskAnalysis/"
      RiskMatrix3x3 <|-- RM3x3S2L1
        click RiskMatrix3x3 href "../RiskMatrix3x3/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * [RiskAnalysis](RiskAnalysis.md)
            * [RiskMatrix](RiskMatrix.md)
                * [RiskMatrix3x3](RiskMatrix3x3.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * **RM3x3S2L1** [ [RiskAnalysis](RiskAnalysis.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RM3x3S2L1](https://w3id.org/lmodel/dpv/risk/RM3x3S2L1) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Low Risk (RM3x3 S:2 L:1)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RM3x3S2L1 |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RM3x3S2L1 |
| native | risk:RM3x3S2L1 |
| exact | dpv_risk:RM3x3S2L1, dpv_risk_owl:RM3x3S2L1 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RM3x3S2L1
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM3x3S2L1
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 3x3 Risk Matrix with Risk Severity: Moderate; Likelihood:
  Low;

  and Risk Level: Low'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Low Risk (RM3x3 S:2 L:1)
exact_mappings:
- dpv_risk:RM3x3S2L1
- dpv_risk_owl:RM3x3S2L1
is_a: RiskMatrix3x3
mixins:
- RiskAnalysis
class_uri: risk:RM3x3S2L1

```
</details>

### Induced

<details>
```yaml
name: RM3x3S2L1
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM3x3S2L1
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 3x3 Risk Matrix with Risk Severity: Moderate; Likelihood:
  Low;

  and Risk Level: Low'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Low Risk (RM3x3 S:2 L:1)
exact_mappings:
- dpv_risk:RM3x3S2L1
- dpv_risk_owl:RM3x3S2L1
is_a: RiskMatrix3x3
mixins:
- RiskAnalysis
class_uri: risk:RM3x3S2L1

```
</details></div>