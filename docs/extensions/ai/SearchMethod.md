---
search:
  boost: 10.0
---

# Class: SearchMethod 


_Refers to statistical-based search Methods_



<div data-search-exclude markdown="1">



URI: [ai:SearchMethod](https://w3id.org/lmodel/dpv/ai/SearchMethod)





```mermaid
 classDiagram
    class SearchMethod
    click SearchMethod href "../SearchMethod/"
      Technique <|-- SearchMethod
        click Technique href "../Technique/"
      StatisticalTechnique <|-- SearchMethod
        click StatisticalTechnique href "../StatisticalTechnique/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [StatisticalTechnique](StatisticalTechnique.md)
            * **SearchMethod** [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SearchMethod](https://w3id.org/lmodel/dpv/ai/SearchMethod) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Search Method




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#SearchMethod |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SearchMethod |
| native | ai:SearchMethod |
| exact | dpv_ai:SearchMethod, dpv_ai_owl:SearchMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SearchMethod
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SearchMethod
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to statistical-based search Methods
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Search Method
exact_mappings:
- dpv_ai:SearchMethod
- dpv_ai_owl:SearchMethod
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:SearchMethod

```
</details>

### Induced

<details>
```yaml
name: SearchMethod
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SearchMethod
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to statistical-based search Methods
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Search Method
exact_mappings:
- dpv_ai:SearchMethod
- dpv_ai_owl:SearchMethod
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:SearchMethod

```
</details></div>