---
search:
  boost: 10.0
---

# Class: SymbolicReasoning 


_Reasoning based on the knowledge encoded in a formal language_



<div data-search-exclude markdown="1">



URI: [ai:SymbolicReasoning](https://w3id.org/lmodel/dpv/ai/SymbolicReasoning)





```mermaid
 classDiagram
    class SymbolicReasoning
    click SymbolicReasoning href "../SymbolicReasoning/"
      Technique <|-- SymbolicReasoning
        click Technique href "../Technique/"
      KnowledgeTechnique <|-- SymbolicReasoning
        click KnowledgeTechnique href "../KnowledgeTechnique/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [KnowledgeTechnique](KnowledgeTechnique.md)
            * **SymbolicReasoning** [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SymbolicReasoning](https://w3id.org/lmodel/dpv/ai/SymbolicReasoning) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Symbolic Reasoning




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#SymbolicReasoning |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SymbolicReasoning |
| native | ai:SymbolicReasoning |
| exact | dpv_ai:SymbolicReasoning, dpv_ai_owl:SymbolicReasoning |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SymbolicReasoning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SymbolicReasoning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Reasoning based on the knowledge encoded in a formal language
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Symbolic Reasoning
exact_mappings:
- dpv_ai:SymbolicReasoning
- dpv_ai_owl:SymbolicReasoning
is_a: KnowledgeTechnique
mixins:
- Technique
class_uri: ai:SymbolicReasoning

```
</details>

### Induced

<details>
```yaml
name: SymbolicReasoning
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SymbolicReasoning
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Reasoning based on the knowledge encoded in a formal language
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Symbolic Reasoning
exact_mappings:
- dpv_ai:SymbolicReasoning
- dpv_ai_owl:SymbolicReasoning
is_a: KnowledgeTechnique
mixins:
- Technique
class_uri: ai:SymbolicReasoning

```
</details></div>