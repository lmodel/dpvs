---
search:
  boost: 10.0
---

# Class: RM7x7S3L2 


_Node in a 7x7 Risk Matrix with Risk Severity: Low; Likelihood: Very Low;_

_and Risk Level: Very Low_



<div data-search-exclude markdown="1">



URI: [risk:RM7x7S3L2](https://w3id.org/lmodel/dpv/risk/RM7x7S3L2)





```mermaid
 classDiagram
    class RM7x7S3L2
    click RM7x7S3L2 href "../RM7x7S3L2/"
      RiskAnalysis <|-- RM7x7S3L2
        click RiskAnalysis href "../RiskAnalysis/"
      RiskMatrix7x7 <|-- RM7x7S3L2
        click RiskMatrix7x7 href "../RiskMatrix7x7/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * [RiskAnalysis](RiskAnalysis.md)
            * [RiskMatrix](RiskMatrix.md)
                * [RiskMatrix7x7](RiskMatrix7x7.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * **RM7x7S3L2** [ [RiskAnalysis](RiskAnalysis.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RM7x7S3L2](https://w3id.org/lmodel/dpv/risk/RM7x7S3L2) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Very Low Risk (RM7x7 S:3 L:2)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RM7x7S3L2 |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RM7x7S3L2 |
| native | risk:RM7x7S3L2 |
| exact | dpv_risk:RM7x7S3L2, dpv_risk_owl:RM7x7S3L2 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RM7x7S3L2
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM7x7S3L2
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 7x7 Risk Matrix with Risk Severity: Low; Likelihood: Very
  Low;

  and Risk Level: Very Low'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very Low Risk (RM7x7 S:3 L:2)
exact_mappings:
- dpv_risk:RM7x7S3L2
- dpv_risk_owl:RM7x7S3L2
is_a: RiskMatrix7x7
mixins:
- RiskAnalysis
class_uri: risk:RM7x7S3L2

```
</details>

### Induced

<details>
```yaml
name: RM7x7S3L2
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM7x7S3L2
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 7x7 Risk Matrix with Risk Severity: Low; Likelihood: Very
  Low;

  and Risk Level: Very Low'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Very Low Risk (RM7x7 S:3 L:2)
exact_mappings:
- dpv_risk:RM7x7S3L2
- dpv_risk_owl:RM7x7S3L2
is_a: RiskMatrix7x7
mixins:
- RiskAnalysis
class_uri: risk:RM7x7S3L2

```
</details></div>