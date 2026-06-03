---
search:
  boost: 10.0
---

# Class: InductiveProgramming 


_An algorithm or program featuring recursive calls or repetition control_

_structures_



<div data-search-exclude markdown="1">



URI: [ai:InductiveProgramming](https://w3id.org/lmodel/dpv/ai/InductiveProgramming)





```mermaid
 classDiagram
    class InductiveProgramming
    click InductiveProgramming href "../InductiveProgramming/"
      Technique <|-- InductiveProgramming
        click Technique href "../Technique/"
      KnowledgeTechnique <|-- InductiveProgramming
        click KnowledgeTechnique href "../KnowledgeTechnique/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [KnowledgeTechnique](KnowledgeTechnique.md)
            * **InductiveProgramming** [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InductiveProgramming](https://w3id.org/lmodel/dpv/ai/InductiveProgramming) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Inductive Programming




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InductiveProgramming |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InductiveProgramming |
| native | ai:InductiveProgramming |
| exact | dpv_ai:InductiveProgramming, dpv_ai_owl:InductiveProgramming |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InductiveProgramming
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InductiveProgramming
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'An algorithm or program featuring recursive calls or repetition control

  structures'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Inductive Programming
exact_mappings:
- dpv_ai:InductiveProgramming
- dpv_ai_owl:InductiveProgramming
is_a: KnowledgeTechnique
mixins:
- Technique
class_uri: ai:InductiveProgramming

```
</details>

### Induced

<details>
```yaml
name: InductiveProgramming
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InductiveProgramming
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'An algorithm or program featuring recursive calls or repetition control

  structures'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Inductive Programming
exact_mappings:
- dpv_ai:InductiveProgramming
- dpv_ai_owl:InductiveProgramming
is_a: KnowledgeTechnique
mixins:
- Technique
class_uri: ai:InductiveProgramming

```
</details></div>