---
search:
  boost: 10.0
---

# Class: DataOperation 


_Processing of data for the development or use of AI models_



<div data-search-exclude markdown="1">



URI: [ai:DataOperation](https://w3id.org/lmodel/dpv/ai/DataOperation)





```mermaid
 classDiagram
    class DataOperation
    click DataOperation href "../DataOperation/"
      DataOperation <|-- DataCollection
        click DataCollection href "../DataCollection/"
      DataOperation <|-- DataPreparation
        click DataPreparation href "../DataPreparation/"
      
      
```





## Inheritance
* **DataOperation**
    * [DataCollection](DataCollection.md)
    * [DataPreparation](DataPreparation.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataOperation](https://w3id.org/lmodel/dpv/ai/DataOperation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* DataOperation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataOperation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataOperation |
| native | ai:DataOperation |
| exact | dpv_ai:DataOperation, dpv_ai_owl:DataOperation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataOperation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataOperation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Processing of data for the development or use of AI models
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- DataOperation
exact_mappings:
- dpv_ai:DataOperation
- dpv_ai_owl:DataOperation
class_uri: ai:DataOperation

```
</details>

### Induced

<details>
```yaml
name: DataOperation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataOperation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Processing of data for the development or use of AI models
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- DataOperation
exact_mappings:
- dpv_ai:DataOperation
- dpv_ai_owl:DataOperation
class_uri: ai:DataOperation

```
</details></div>