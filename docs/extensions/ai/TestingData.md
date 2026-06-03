---
search:
  boost: 10.0
---

# Class: TestingData 


_Data involved in the testing of an AI system or model_



<div data-search-exclude markdown="1">



URI: [ai:TestingData](https://w3id.org/lmodel/dpv/ai/TestingData)





```mermaid
 classDiagram
    class TestingData
    click TestingData href "../TestingData/"
      DpvData <|-- TestingData
        click DpvData href "../DpvData/"
      
      
```





## Inheritance
* [DpvData](DpvData.md)
    * **TestingData**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingData](https://w3id.org/lmodel/dpv/ai/TestingData) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingData |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingData |
| native | ai:TestingData |
| exact | dpv_ai:TestingData, dpv_ai_owl:TestingData |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Data involved in the testing of an AI system or model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data
exact_mappings:
- dpv_ai:TestingData
- dpv_ai_owl:TestingData
is_a: DpvData
class_uri: ai:TestingData

```
</details>

### Induced

<details>
```yaml
name: TestingData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingData
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Data involved in the testing of an AI system or model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data
exact_mappings:
- dpv_ai:TestingData
- dpv_ai_owl:TestingData
is_a: DpvData
class_uri: ai:TestingData

```
</details></div>