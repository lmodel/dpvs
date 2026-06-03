---
search:
  boost: 10.0
---

# Class: BiasAssessment 


_Examination of a data set, model, or AI system for bias_



<div data-search-exclude markdown="1">



URI: [ai:BiasAssessment](https://w3id.org/lmodel/dpv/ai/BiasAssessment)





```mermaid
 classDiagram
    class BiasAssessment
    click BiasAssessment href "../BiasAssessment/"
      BiasAssessment <|-- BiasDetection
        click BiasDetection href "../BiasDetection/"
      BiasAssessment <|-- BiasMitigation
        click BiasMitigation href "../BiasMitigation/"
      BiasAssessment <|-- BiasPrevention
        click BiasPrevention href "../BiasPrevention/"
      
      
```





## Inheritance
* **BiasAssessment**
    * [BiasDetection](BiasDetection.md)
    * [BiasMitigation](BiasMitigation.md)
    * [BiasPrevention](BiasPrevention.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BiasAssessment](https://w3id.org/lmodel/dpv/ai/BiasAssessment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Bias Assessment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BiasAssessment |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BiasAssessment |
| native | ai:BiasAssessment |
| exact | dpv_ai:BiasAssessment, dpv_ai_owl:BiasAssessment |
| close | iso42001:AISystemImpactAssessment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiasAssessment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiasAssessment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Examination of a data set, model, or AI system for bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bias Assessment
exact_mappings:
- dpv_ai:BiasAssessment
- dpv_ai_owl:BiasAssessment
close_mappings:
- iso42001:AISystemImpactAssessment
class_uri: ai:BiasAssessment

```
</details>

### Induced

<details>
```yaml
name: BiasAssessment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiasAssessment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Examination of a data set, model, or AI system for bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bias Assessment
exact_mappings:
- dpv_ai:BiasAssessment
- dpv_ai_owl:BiasAssessment
close_mappings:
- iso42001:AISystemImpactAssessment
class_uri: ai:BiasAssessment

```
</details></div>