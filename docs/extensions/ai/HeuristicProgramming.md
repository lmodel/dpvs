---
search:
  boost: 10.0
---

# Class: HeuristicProgramming 


_Programming approach designed to tackle problems for which there lacks a_

_systematic or optimized approach, frequently used in expert systems_



<div data-search-exclude markdown="1">



URI: [ai:HeuristicProgramming](https://w3id.org/lmodel/dpv/ai/HeuristicProgramming)





```mermaid
 classDiagram
    class HeuristicProgramming
    click HeuristicProgramming href "../HeuristicProgramming/"
      Technique <|-- HeuristicProgramming
        click Technique href "../Technique/"
      RuleBasedTechnique <|-- HeuristicProgramming
        click RuleBasedTechnique href "../RuleBasedTechnique/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [KnowledgeTechnique](KnowledgeTechnique.md)
            * [RuleBasedTechnique](RuleBasedTechnique.md) [ [Technique](Technique.md)]
                * **HeuristicProgramming** [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:HeuristicProgramming](https://w3id.org/lmodel/dpv/ai/HeuristicProgramming) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Heuristic Programming




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#HeuristicProgramming |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:HeuristicProgramming |
| native | ai:HeuristicProgramming |
| exact | dpv_ai:HeuristicProgramming, dpv_ai_owl:HeuristicProgramming |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HeuristicProgramming
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#HeuristicProgramming
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Programming approach designed to tackle problems for which there lacks
  a

  systematic or optimized approach, frequently used in expert systems'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Heuristic Programming
exact_mappings:
- dpv_ai:HeuristicProgramming
- dpv_ai_owl:HeuristicProgramming
is_a: RuleBasedTechnique
mixins:
- Technique
class_uri: ai:HeuristicProgramming

```
</details>

### Induced

<details>
```yaml
name: HeuristicProgramming
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#HeuristicProgramming
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Programming approach designed to tackle problems for which there lacks
  a

  systematic or optimized approach, frequently used in expert systems'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Heuristic Programming
exact_mappings:
- dpv_ai:HeuristicProgramming
- dpv_ai_owl:HeuristicProgramming
is_a: RuleBasedTechnique
mixins:
- Technique
class_uri: ai:HeuristicProgramming

```
</details></div>