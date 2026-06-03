---
search:
  boost: 10.0
---

# Class: DataAggregationBias 


_Bias that occurs from aggregating data covering different groups of_

_objects that might have different statistical distributions which_

_introduce bias into the data used to train AI systems_



<div data-search-exclude markdown="1">



URI: [ai:DataAggregationBias](https://w3id.org/lmodel/dpv/ai/DataAggregationBias)





```mermaid
 classDiagram
    class DataAggregationBias
    click DataAggregationBias href "../DataAggregationBias/"
      RiskConcept <|-- DataAggregationBias
        click RiskConcept href "../RiskConcept/"
      DataBias <|-- DataAggregationBias
        click DataBias href "../DataBias/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [AIBias](AIBias.md)
        * [DataBias](DataBias.md) [ [RiskConcept](RiskConcept.md)]
            * **DataAggregationBias** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataAggregationBias](https://w3id.org/lmodel/dpv/ai/DataAggregationBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Aggregation Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataAggregationBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataAggregationBias |
| native | ai:DataAggregationBias |
| exact | dpv_ai:DataAggregationBias, dpv_ai_owl:DataAggregationBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataAggregationBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataAggregationBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs from aggregating data covering different groups of

  objects that might have different statistical distributions which

  introduce bias into the data used to train AI systems'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Aggregation Bias
exact_mappings:
- dpv_ai:DataAggregationBias
- dpv_ai_owl:DataAggregationBias
is_a: DataBias
mixins:
- RiskConcept
class_uri: ai:DataAggregationBias

```
</details>

### Induced

<details>
```yaml
name: DataAggregationBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataAggregationBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs from aggregating data covering different groups of

  objects that might have different statistical distributions which

  introduce bias into the data used to train AI systems'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Aggregation Bias
exact_mappings:
- dpv_ai:DataAggregationBias
- dpv_ai_owl:DataAggregationBias
is_a: DataBias
mixins:
- RiskConcept
class_uri: ai:DataAggregationBias

```
</details></div>