---
search:
  boost: 10.0
---

# Class: LLM 


_Deep learning model that uses artificial neural networks trained on vast_

_amounts of data to understand and generate natural language and other_

_types of content to perform a wide range of tasks_



<div data-search-exclude markdown="1">



URI: [ai:LLM](https://w3id.org/lmodel/dpv/ai/LLM)





```mermaid
 classDiagram
    class LLM
    click LLM href "../LLM/"
      Model <|-- LLM
        click Model href "../Model/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Model](Model.md)
        * **LLM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:LLM](https://w3id.org/lmodel/dpv/ai/LLM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Large Language Model (LLM)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#LLM |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:LLM |
| native | ai:LLM |
| exact | dpv_ai:LLM, dpv_ai_owl:LLM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LLM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LLM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Deep learning model that uses artificial neural networks trained on
  vast

  amounts of data to understand and generate natural language and other

  types of content to perform a wide range of tasks'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Large Language Model (LLM)
exact_mappings:
- dpv_ai:LLM
- dpv_ai_owl:LLM
is_a: Model
class_uri: ai:LLM

```
</details>

### Induced

<details>
```yaml
name: LLM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LLM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Deep learning model that uses artificial neural networks trained on
  vast

  amounts of data to understand and generate natural language and other

  types of content to perform a wide range of tasks'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Large Language Model (LLM)
exact_mappings:
- dpv_ai:LLM
- dpv_ai_owl:LLM
is_a: Model
class_uri: ai:LLM

```
</details></div>