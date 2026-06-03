---
search:
  boost: 10.0
---

# Class: BiasPrevention 


_Indicates measures to prevent bias_



<div data-search-exclude markdown="1">



URI: [ai:BiasPrevention](https://w3id.org/lmodel/dpv/ai/BiasPrevention)





```mermaid
 classDiagram
    class BiasPrevention
    click BiasPrevention href "../BiasPrevention/"
      BiasAssessment <|-- BiasPrevention
        click BiasAssessment href "../BiasAssessment/"
      
      
```





## Inheritance
* [BiasAssessment](BiasAssessment.md)
    * **BiasPrevention**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BiasPrevention](https://w3id.org/lmodel/dpv/ai/BiasPrevention) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Bias Prevention




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BiasPrevention |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BiasPrevention |
| native | ai:BiasPrevention |
| exact | dpv_ai:BiasPrevention, dpv_ai_owl:BiasPrevention |
| close | iso42001:AIRiskTreatmentPlan |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiasPrevention
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiasPrevention
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates measures to prevent bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bias Prevention
exact_mappings:
- dpv_ai:BiasPrevention
- dpv_ai_owl:BiasPrevention
close_mappings:
- iso42001:AIRiskTreatmentPlan
is_a: BiasAssessment
class_uri: ai:BiasPrevention

```
</details>

### Induced

<details>
```yaml
name: BiasPrevention
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiasPrevention
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates measures to prevent bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bias Prevention
exact_mappings:
- dpv_ai:BiasPrevention
- dpv_ai_owl:BiasPrevention
close_mappings:
- iso42001:AIRiskTreatmentPlan
is_a: BiasAssessment
class_uri: ai:BiasPrevention

```
</details></div>