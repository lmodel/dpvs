---
search:
  boost: 10.0
---

# Class: OptimisationMethod 


_Refers to optimisation Method_



<div data-search-exclude markdown="1">



URI: [ai:OptimisationMethod](https://w3id.org/lmodel/dpv/ai/OptimisationMethod)





```mermaid
 classDiagram
    class OptimisationMethod
    click OptimisationMethod href "../OptimisationMethod/"
      Technique <|-- OptimisationMethod
        click Technique href "../Technique/"
      StatisticalTechnique <|-- OptimisationMethod
        click StatisticalTechnique href "../StatisticalTechnique/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [StatisticalTechnique](StatisticalTechnique.md)
            * **OptimisationMethod** [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:OptimisationMethod](https://w3id.org/lmodel/dpv/ai/OptimisationMethod) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Optimisation Method




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#OptimisationMethod |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:OptimisationMethod |
| native | ai:OptimisationMethod |
| exact | dpv_ai:OptimisationMethod, dpv_ai_owl:OptimisationMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OptimisationMethod
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#OptimisationMethod
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to optimisation Method
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Optimisation Method
exact_mappings:
- dpv_ai:OptimisationMethod
- dpv_ai_owl:OptimisationMethod
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:OptimisationMethod

```
</details>

### Induced

<details>
```yaml
name: OptimisationMethod
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#OptimisationMethod
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to optimisation Method
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Optimisation Method
exact_mappings:
- dpv_ai:OptimisationMethod
- dpv_ai_owl:OptimisationMethod
is_a: StatisticalTechnique
mixins:
- Technique
class_uri: ai:OptimisationMethod

```
</details></div>