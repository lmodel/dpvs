---
search:
  boost: 10.0
---

# Class: DpvData 


_Data involved in the development and use of an AI system or model_



<div data-search-exclude markdown="1">



URI: [ai:Data](https://w3id.org/lmodel/dpv/ai/Data)





```mermaid
 classDiagram
    class DpvData
    click DpvData href "../DpvData/"
      DpvData <|-- TestingData
        click TestingData href "../TestingData/"
      DpvData <|-- TrainingData
        click TrainingData href "../TrainingData/"
      DpvData <|-- ValidationData
        click ValidationData href "../ValidationData/"
      
      
```





## Inheritance
* **DpvData**
    * [TestingData](TestingData.md)
    * [TrainingData](TrainingData.md)
    * [ValidationData](ValidationData.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:Data](https://w3id.org/lmodel/dpv/ai/Data) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data
* AI Data




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#Data |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:Data |
| native | ai:DpvData |
| exact | dpv_ai:Data, dpv_ai_owl:Data |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#Data
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Data involved in the development and use of an AI system or model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data
- AI Data
exact_mappings:
- dpv_ai:Data
- dpv_ai_owl:Data
class_uri: ai:Data

```
</details>

### Induced

<details>
```yaml
name: DpvData
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#Data
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Data involved in the development and use of an AI system or model
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data
- AI Data
exact_mappings:
- dpv_ai:Data
- dpv_ai_owl:Data
class_uri: ai:Data

```
</details></div>