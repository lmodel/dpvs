---
search:
  boost: 10.0
---

# Class: InputDataBias 


_Concept representing input data containing or potentially containing_

_bias_



<div data-search-exclude markdown="1">



URI: [ai:InputDataBias](https://w3id.org/lmodel/dpv/ai/InputDataBias)





```mermaid
 classDiagram
    class InputDataBias
    click InputDataBias href "../InputDataBias/"
      RiskConcept <|-- InputDataBias
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataBias
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataBias** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataBias](https://w3id.org/lmodel/dpv/ai/InputDataBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataBias |
| native | ai:InputDataBias |
| exact | dpv_ai:InputDataBias, dpv_ai_owl:InputDataBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataBias
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Concept representing input data containing or potentially containing

  bias'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Bias
exact_mappings:
- dpv_ai:InputDataBias
- dpv_ai_owl:InputDataBias
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataBias

```
</details>

### Induced

<details>
```yaml
name: InputDataBias
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Concept representing input data containing or potentially containing

  bias'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Bias
exact_mappings:
- dpv_ai:InputDataBias
- dpv_ai_owl:InputDataBias
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataBias

```
</details></div>