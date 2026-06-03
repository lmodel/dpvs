---
search:
  boost: 10.0
---

# Class: DataLabellingProcessBias 


_Bias that occurs due to the labelling process itself introducing_

_societal or cognitive biases_



<div data-search-exclude markdown="1">



URI: [ai:DataLabellingProcessBias](https://w3id.org/lmodel/dpv/ai/DataLabellingProcessBias)





```mermaid
 classDiagram
    class DataLabellingProcessBias
    click DataLabellingProcessBias href "../DataLabellingProcessBias/"
      RiskConcept <|-- DataLabellingProcessBias
        click RiskConcept href "../RiskConcept/"
      DataBias <|-- DataLabellingProcessBias
        click DataBias href "../DataBias/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [AIBias](AIBias.md)
        * [DataBias](DataBias.md) [ [RiskConcept](RiskConcept.md)]
            * **DataLabellingProcessBias** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataLabellingProcessBias](https://w3id.org/lmodel/dpv/ai/DataLabellingProcessBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Labelling Process Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataLabellingProcessBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataLabellingProcessBias |
| native | ai:DataLabellingProcessBias |
| exact | dpv_ai:DataLabellingProcessBias, dpv_ai_owl:DataLabellingProcessBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataLabellingProcessBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataLabellingProcessBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to the labelling process itself introducing

  societal or cognitive biases'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Labelling Process Bias
exact_mappings:
- dpv_ai:DataLabellingProcessBias
- dpv_ai_owl:DataLabellingProcessBias
is_a: DataBias
mixins:
- RiskConcept
class_uri: ai:DataLabellingProcessBias

```
</details>

### Induced

<details>
```yaml
name: DataLabellingProcessBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataLabellingProcessBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to the labelling process itself introducing

  societal or cognitive biases'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Labelling Process Bias
exact_mappings:
- dpv_ai:DataLabellingProcessBias
- dpv_ai_owl:DataLabellingProcessBias
is_a: DataBias
mixins:
- RiskConcept
class_uri: ai:DataLabellingProcessBias

```
</details></div>