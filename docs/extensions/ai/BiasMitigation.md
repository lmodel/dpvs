---
search:
  boost: 10.0
---

# Class: BiasMitigation 


_Indicates measures to mitigate bias_



<div data-search-exclude markdown="1">



URI: [ai:BiasMitigation](https://w3id.org/lmodel/dpv/ai/BiasMitigation)





```mermaid
 classDiagram
    class BiasMitigation
    click BiasMitigation href "../BiasMitigation/"
      BiasAssessment <|-- BiasMitigation
        click BiasAssessment href "../BiasAssessment/"
      
      
```





## Inheritance
* [BiasAssessment](BiasAssessment.md)
    * **BiasMitigation**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BiasMitigation](https://w3id.org/lmodel/dpv/ai/BiasMitigation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Bias Mitigation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BiasMitigation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BiasMitigation |
| native | ai:BiasMitigation |
| exact | dpv_ai:BiasMitigation, dpv_ai_owl:BiasMitigation |
| close | iso42001:AIRiskTreatmentPlan |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiasMitigation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiasMitigation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates measures to mitigate bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bias Mitigation
exact_mappings:
- dpv_ai:BiasMitigation
- dpv_ai_owl:BiasMitigation
close_mappings:
- iso42001:AIRiskTreatmentPlan
is_a: BiasAssessment
class_uri: ai:BiasMitigation

```
</details>

### Induced

<details>
```yaml
name: BiasMitigation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiasMitigation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates measures to mitigate bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bias Mitigation
exact_mappings:
- dpv_ai:BiasMitigation
- dpv_ai_owl:BiasMitigation
close_mappings:
- iso42001:AIRiskTreatmentPlan
is_a: BiasAssessment
class_uri: ai:BiasMitigation

```
</details></div>