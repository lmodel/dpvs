---
search:
  boost: 10.0
---

# Class: RiskMatrix7x7 


_A Risk Matrix with 7 Likelihood, 7 Severity, and 7 Risk Level types_



<div data-search-exclude markdown="1">



URI: [risk:RiskMatrix7x7](https://w3id.org/lmodel/dpv/risk/RiskMatrix7x7)





```mermaid
 classDiagram
    class RiskMatrix7x7
    click RiskMatrix7x7 href "../RiskMatrix7x7/"
      RiskAnalysis <|-- RiskMatrix7x7
        click RiskAnalysis href "../RiskAnalysis/"
      RiskMatrix <|-- RiskMatrix7x7
        click RiskMatrix href "../RiskMatrix/"
      

      RiskMatrix7x7 <|-- RM7x7S1L1
        click RM7x7S1L1 href "../RM7x7S1L1/"
      RiskMatrix7x7 <|-- RM7x7S1L2
        click RM7x7S1L2 href "../RM7x7S1L2/"
      RiskMatrix7x7 <|-- RM7x7S1L3
        click RM7x7S1L3 href "../RM7x7S1L3/"
      RiskMatrix7x7 <|-- RM7x7S1L4
        click RM7x7S1L4 href "../RM7x7S1L4/"
      RiskMatrix7x7 <|-- RM7x7S1L5
        click RM7x7S1L5 href "../RM7x7S1L5/"
      RiskMatrix7x7 <|-- RM7x7S1L6
        click RM7x7S1L6 href "../RM7x7S1L6/"
      RiskMatrix7x7 <|-- RM7x7S1L7
        click RM7x7S1L7 href "../RM7x7S1L7/"
      RiskMatrix7x7 <|-- RM7x7S2L1
        click RM7x7S2L1 href "../RM7x7S2L1/"
      RiskMatrix7x7 <|-- RM7x7S2L2
        click RM7x7S2L2 href "../RM7x7S2L2/"
      RiskMatrix7x7 <|-- RM7x7S2L3
        click RM7x7S2L3 href "../RM7x7S2L3/"
      RiskMatrix7x7 <|-- RM7x7S2L4
        click RM7x7S2L4 href "../RM7x7S2L4/"
      RiskMatrix7x7 <|-- RM7x7S2L5
        click RM7x7S2L5 href "../RM7x7S2L5/"
      RiskMatrix7x7 <|-- RM7x7S2L6
        click RM7x7S2L6 href "../RM7x7S2L6/"
      RiskMatrix7x7 <|-- RM7x7S2L7
        click RM7x7S2L7 href "../RM7x7S2L7/"
      RiskMatrix7x7 <|-- RM7x7S3L1
        click RM7x7S3L1 href "../RM7x7S3L1/"
      RiskMatrix7x7 <|-- RM7x7S3L2
        click RM7x7S3L2 href "../RM7x7S3L2/"
      RiskMatrix7x7 <|-- RM7x7S3L3
        click RM7x7S3L3 href "../RM7x7S3L3/"
      RiskMatrix7x7 <|-- RM7x7S3L4
        click RM7x7S3L4 href "../RM7x7S3L4/"
      RiskMatrix7x7 <|-- RM7x7S3L5
        click RM7x7S3L5 href "../RM7x7S3L5/"
      RiskMatrix7x7 <|-- RM7x7S3L6
        click RM7x7S3L6 href "../RM7x7S3L6/"
      RiskMatrix7x7 <|-- RM7x7S3L7
        click RM7x7S3L7 href "../RM7x7S3L7/"
      RiskMatrix7x7 <|-- RM7x7S4L1
        click RM7x7S4L1 href "../RM7x7S4L1/"
      RiskMatrix7x7 <|-- RM7x7S4L2
        click RM7x7S4L2 href "../RM7x7S4L2/"
      RiskMatrix7x7 <|-- RM7x7S4L3
        click RM7x7S4L3 href "../RM7x7S4L3/"
      RiskMatrix7x7 <|-- RM7x7S4L4
        click RM7x7S4L4 href "../RM7x7S4L4/"
      RiskMatrix7x7 <|-- RM7x7S4L5
        click RM7x7S4L5 href "../RM7x7S4L5/"
      RiskMatrix7x7 <|-- RM7x7S4L6
        click RM7x7S4L6 href "../RM7x7S4L6/"
      RiskMatrix7x7 <|-- RM7x7S4L7
        click RM7x7S4L7 href "../RM7x7S4L7/"
      RiskMatrix7x7 <|-- RM7x7S5L1
        click RM7x7S5L1 href "../RM7x7S5L1/"
      RiskMatrix7x7 <|-- RM7x7S5L2
        click RM7x7S5L2 href "../RM7x7S5L2/"
      RiskMatrix7x7 <|-- RM7x7S5L3
        click RM7x7S5L3 href "../RM7x7S5L3/"
      RiskMatrix7x7 <|-- RM7x7S5L4
        click RM7x7S5L4 href "../RM7x7S5L4/"
      RiskMatrix7x7 <|-- RM7x7S5L5
        click RM7x7S5L5 href "../RM7x7S5L5/"
      RiskMatrix7x7 <|-- RM7x7S5L6
        click RM7x7S5L6 href "../RM7x7S5L6/"
      RiskMatrix7x7 <|-- RM7x7S5L7
        click RM7x7S5L7 href "../RM7x7S5L7/"
      RiskMatrix7x7 <|-- RM7x7S6L1
        click RM7x7S6L1 href "../RM7x7S6L1/"
      RiskMatrix7x7 <|-- RM7x7S6L2
        click RM7x7S6L2 href "../RM7x7S6L2/"
      RiskMatrix7x7 <|-- RM7x7S6L3
        click RM7x7S6L3 href "../RM7x7S6L3/"
      RiskMatrix7x7 <|-- RM7x7S6L4
        click RM7x7S6L4 href "../RM7x7S6L4/"
      RiskMatrix7x7 <|-- RM7x7S6L5
        click RM7x7S6L5 href "../RM7x7S6L5/"
      RiskMatrix7x7 <|-- RM7x7S6L6
        click RM7x7S6L6 href "../RM7x7S6L6/"
      RiskMatrix7x7 <|-- RM7x7S6L7
        click RM7x7S6L7 href "../RM7x7S6L7/"
      RiskMatrix7x7 <|-- RM7x7S7L1
        click RM7x7S7L1 href "../RM7x7S7L1/"
      RiskMatrix7x7 <|-- RM7x7S7L2
        click RM7x7S7L2 href "../RM7x7S7L2/"
      RiskMatrix7x7 <|-- RM7x7S7L3
        click RM7x7S7L3 href "../RM7x7S7L3/"
      RiskMatrix7x7 <|-- RM7x7S7L4
        click RM7x7S7L4 href "../RM7x7S7L4/"
      RiskMatrix7x7 <|-- RM7x7S7L5
        click RM7x7S7L5 href "../RM7x7S7L5/"
      RiskMatrix7x7 <|-- RM7x7S7L6
        click RM7x7S7L6 href "../RM7x7S7L6/"
      RiskMatrix7x7 <|-- RM7x7S7L7
        click RM7x7S7L7 href "../RM7x7S7L7/"
      

      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * [RiskAnalysis](RiskAnalysis.md)
            * [RiskMatrix](RiskMatrix.md)
                * **RiskMatrix7x7** [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S1L1](RM7x7S1L1.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S1L2](RM7x7S1L2.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S1L3](RM7x7S1L3.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S1L4](RM7x7S1L4.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S1L5](RM7x7S1L5.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S1L6](RM7x7S1L6.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S1L7](RM7x7S1L7.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S2L1](RM7x7S2L1.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S2L2](RM7x7S2L2.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S2L3](RM7x7S2L3.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S2L4](RM7x7S2L4.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S2L5](RM7x7S2L5.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S2L6](RM7x7S2L6.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S2L7](RM7x7S2L7.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S3L1](RM7x7S3L1.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S3L2](RM7x7S3L2.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S3L3](RM7x7S3L3.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S3L4](RM7x7S3L4.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S3L5](RM7x7S3L5.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S3L6](RM7x7S3L6.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S3L7](RM7x7S3L7.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S4L1](RM7x7S4L1.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S4L2](RM7x7S4L2.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S4L3](RM7x7S4L3.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S4L4](RM7x7S4L4.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S4L5](RM7x7S4L5.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S4L6](RM7x7S4L6.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S4L7](RM7x7S4L7.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S5L1](RM7x7S5L1.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S5L2](RM7x7S5L2.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S5L3](RM7x7S5L3.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S5L4](RM7x7S5L4.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S5L5](RM7x7S5L5.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S5L6](RM7x7S5L6.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S5L7](RM7x7S5L7.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S6L1](RM7x7S6L1.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S6L2](RM7x7S6L2.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S6L3](RM7x7S6L3.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S6L4](RM7x7S6L4.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S6L5](RM7x7S6L5.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S6L6](RM7x7S6L6.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S6L7](RM7x7S6L7.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S7L1](RM7x7S7L1.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S7L2](RM7x7S7L2.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S7L3](RM7x7S7L3.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S7L4](RM7x7S7L4.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S7L5](RM7x7S7L5.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S7L6](RM7x7S7L6.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * [RM7x7S7L7](RM7x7S7L7.md) [ [RiskAnalysis](RiskAnalysis.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RiskMatrix7x7](https://w3id.org/lmodel/dpv/risk/RiskMatrix7x7) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Risk Matrix 7x7




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RiskMatrix7x7 |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RiskMatrix7x7 |
| native | risk:RiskMatrix7x7 |
| exact | dpv_risk:RiskMatrix7x7, dpv_risk_owl:RiskMatrix7x7 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskMatrix7x7
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskMatrix7x7
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: A Risk Matrix with 7 Likelihood, 7 Severity, and 7 Risk Level types
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Matrix 7x7
exact_mappings:
- dpv_risk:RiskMatrix7x7
- dpv_risk_owl:RiskMatrix7x7
is_a: RiskMatrix
mixins:
- RiskAnalysis
class_uri: risk:RiskMatrix7x7

```
</details>

### Induced

<details>
```yaml
name: RiskMatrix7x7
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskMatrix7x7
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: A Risk Matrix with 7 Likelihood, 7 Severity, and 7 Risk Level types
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Matrix 7x7
exact_mappings:
- dpv_risk:RiskMatrix7x7
- dpv_risk_owl:RiskMatrix7x7
is_a: RiskMatrix
mixins:
- RiskAnalysis
class_uri: risk:RiskMatrix7x7

```
</details></div>