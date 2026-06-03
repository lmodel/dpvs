---
search:
  boost: 10.0
---

# Class: RiskEvaluation 


_Process determining acceptability or tolerance of risk by comparing risk_

_analysis outcomes against risk criteria_



<div data-search-exclude markdown="1">



URI: [risk:RiskEvaluation](https://w3id.org/lmodel/dpv/risk/RiskEvaluation)





```mermaid
 classDiagram
    class RiskEvaluation
    click RiskEvaluation href "../RiskEvaluation/"
      RiskAssessment <|-- RiskEvaluation
        click RiskAssessment href "../RiskAssessment/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * **RiskEvaluation**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RiskEvaluation](https://w3id.org/lmodel/dpv/risk/RiskEvaluation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Risk Evaluation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RiskEvaluation |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RiskEvaluation |
| native | risk:RiskEvaluation |
| exact | dpv_risk:RiskEvaluation, dpv_risk_owl:RiskEvaluation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskEvaluation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskEvaluation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Process determining acceptability or tolerance of risk by comparing
  risk

  analysis outcomes against risk criteria'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Evaluation
exact_mappings:
- dpv_risk:RiskEvaluation
- dpv_risk_owl:RiskEvaluation
is_a: RiskAssessment
class_uri: risk:RiskEvaluation

```
</details>

### Induced

<details>
```yaml
name: RiskEvaluation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskEvaluation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Process determining acceptability or tolerance of risk by comparing
  risk

  analysis outcomes against risk criteria'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Evaluation
exact_mappings:
- dpv_risk:RiskEvaluation
- dpv_risk_owl:RiskEvaluation
is_a: RiskAssessment
class_uri: risk:RiskEvaluation

```
</details></div>