---
search:
  boost: 10.0
---

# Class: DataBias 


_Bias that occurs due to unaddressed data properties that lead to AI_

_systems that perform better or worse for different groups_



<div data-search-exclude markdown="1">



URI: [ai:DataBias](https://w3id.org/lmodel/dpv/ai/DataBias)





```mermaid
 classDiagram
    class DataBias
    click DataBias href "../DataBias/"
      RiskConcept <|-- DataBias
        click RiskConcept href "../RiskConcept/"
      AIBias <|-- DataBias
        click AIBias href "../AIBias/"
      

      DataBias <|-- DataAggregationBias
        click DataAggregationBias href "../DataAggregationBias/"
      DataBias <|-- DataLabellingProcessBias
        click DataLabellingProcessBias href "../DataLabellingProcessBias/"
      DataBias <|-- DistributedTrainingBias
        click DistributedTrainingBias href "../DistributedTrainingBias/"
      DataBias <|-- MissingFeaturesBias
        click MissingFeaturesBias href "../MissingFeaturesBias/"
      DataBias <|-- NonRepresentativeSamplingBias
        click NonRepresentativeSamplingBias href "../NonRepresentativeSamplingBias/"
      

      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [AIBias](AIBias.md)
        * **DataBias** [ [RiskConcept](RiskConcept.md)]
            * [DataAggregationBias](DataAggregationBias.md) [ [RiskConcept](RiskConcept.md)]
            * [DataLabellingProcessBias](DataLabellingProcessBias.md) [ [RiskConcept](RiskConcept.md)]
            * [DistributedTrainingBias](DistributedTrainingBias.md) [ [RiskConcept](RiskConcept.md)]
            * [MissingFeaturesBias](MissingFeaturesBias.md) [ [RiskConcept](RiskConcept.md)]
            * [NonRepresentativeSamplingBias](NonRepresentativeSamplingBias.md) [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataBias](https://w3id.org/lmodel/dpv/ai/DataBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataBias |
| native | ai:DataBias |
| exact | dpv_ai:DataBias, dpv_ai_owl:DataBias |
| related | iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to unaddressed data properties that lead to AI

  systems that perform better or worse for different groups'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Bias
exact_mappings:
- dpv_ai:DataBias
- dpv_ai_owl:DataBias
related_mappings:
- iso42001:AIRisk
is_a: AIBias
mixins:
- RiskConcept
class_uri: ai:DataBias

```
</details>

### Induced

<details>
```yaml
name: DataBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to unaddressed data properties that lead to AI

  systems that perform better or worse for different groups'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Bias
exact_mappings:
- dpv_ai:DataBias
- dpv_ai_owl:DataBias
related_mappings:
- iso42001:AIRisk
is_a: AIBias
mixins:
- RiskConcept
class_uri: ai:DataBias

```
</details></div>