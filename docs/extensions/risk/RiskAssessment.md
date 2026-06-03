---
search:
  boost: 10.0
---

# Class: RiskAssessment 


_Assessment of risk involving its identification, analysis, and_

_evaluation_



<div data-search-exclude markdown="1">



URI: [risk:RiskAssessment](https://w3id.org/lmodel/dpv/risk/RiskAssessment)





```mermaid
 classDiagram
    class RiskAssessment
    click RiskAssessment href "../RiskAssessment/"
      RiskManagement <|-- RiskAssessment
        click RiskManagement href "../RiskManagement/"
      

      RiskAssessment <|-- RiskAnalysis
        click RiskAnalysis href "../RiskAnalysis/"
      RiskAssessment <|-- RiskEvaluation
        click RiskEvaluation href "../RiskEvaluation/"
      RiskAssessment <|-- RiskIdentification
        click RiskIdentification href "../RiskIdentification/"
      

      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * **RiskAssessment**
        * [RiskAnalysis](RiskAnalysis.md)
        * [RiskEvaluation](RiskEvaluation.md)
        * [RiskIdentification](RiskIdentification.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RiskAssessment](https://w3id.org/lmodel/dpv/risk/RiskAssessment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Risk Assessment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO 31073:2022 Risk management vocabulary |
| upstream_iri | https://w3id.org/dpv/risk/owl#RiskAssessment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RiskAssessment |
| native | risk:RiskAssessment |
| exact | dpv_risk:RiskAssessment, dpv_risk_owl:RiskAssessment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskAssessment
annotations:
  dct_source:
    tag: dct_source
    value: ISO 31073:2022 Risk management vocabulary
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskAssessment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Assessment of risk involving its identification, analysis, and

  evaluation'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Assessment
exact_mappings:
- dpv_risk:RiskAssessment
- dpv_risk_owl:RiskAssessment
is_a: RiskManagement
class_uri: risk:RiskAssessment

```
</details>

### Induced

<details>
```yaml
name: RiskAssessment
annotations:
  dct_source:
    tag: dct_source
    value: ISO 31073:2022 Risk management vocabulary
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskAssessment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Assessment of risk involving its identification, analysis, and

  evaluation'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Assessment
exact_mappings:
- dpv_risk:RiskAssessment
- dpv_risk_owl:RiskAssessment
is_a: RiskManagement
class_uri: risk:RiskAssessment

```
</details></div>