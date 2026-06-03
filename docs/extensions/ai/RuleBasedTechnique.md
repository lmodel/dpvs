---
search:
  boost: 10.0
---

# Class: RuleBasedTechnique 


_Artificial intelligence approach governed by human-defined rules that_

_explicitly dictate behaviour, relying on logical statements (rules) to_

_determine actions in specific situations_



<div data-search-exclude markdown="1">



URI: [ai:RuleBasedTechnique](https://w3id.org/lmodel/dpv/ai/RuleBasedTechnique)





```mermaid
 classDiagram
    class RuleBasedTechnique
    click RuleBasedTechnique href "../RuleBasedTechnique/"
      Technique <|-- RuleBasedTechnique
        click Technique href "../Technique/"
      KnowledgeTechnique <|-- RuleBasedTechnique
        click KnowledgeTechnique href "../KnowledgeTechnique/"
      

      RuleBasedTechnique <|-- HeuristicProgramming
        click HeuristicProgramming href "../HeuristicProgramming/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * [KnowledgeTechnique](KnowledgeTechnique.md)
            * **RuleBasedTechnique** [ [Technique](Technique.md)]
                * [HeuristicProgramming](HeuristicProgramming.md) [ [Technique](Technique.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:RuleBasedTechnique](https://w3id.org/lmodel/dpv/ai/RuleBasedTechnique) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Rule Technique




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#RuleBasedTechnique |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:RuleBasedTechnique |
| native | ai:RuleBasedTechnique |
| exact | dpv_ai:RuleBasedTechnique, dpv_ai_owl:RuleBasedTechnique |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RuleBasedTechnique
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RuleBasedTechnique
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Artificial intelligence approach governed by human-defined rules that

  explicitly dictate behaviour, relying on logical statements (rules) to

  determine actions in specific situations'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Rule Technique
exact_mappings:
- dpv_ai:RuleBasedTechnique
- dpv_ai_owl:RuleBasedTechnique
is_a: KnowledgeTechnique
mixins:
- Technique
class_uri: ai:RuleBasedTechnique

```
</details>

### Induced

<details>
```yaml
name: RuleBasedTechnique
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RuleBasedTechnique
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Artificial intelligence approach governed by human-defined rules that

  explicitly dictate behaviour, relying on logical statements (rules) to

  determine actions in specific situations'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Rule Technique
exact_mappings:
- dpv_ai:RuleBasedTechnique
- dpv_ai_owl:RuleBasedTechnique
is_a: KnowledgeTechnique
mixins:
- Technique
class_uri: ai:RuleBasedTechnique

```
</details></div>