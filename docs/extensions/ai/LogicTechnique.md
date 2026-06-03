---
search:
  boost: 10.0
---

# Class: LogicTechnique 


_Refers to logic based techniques_



<div data-search-exclude markdown="1">



URI: [ai:LogicTechnique](https://w3id.org/lmodel/dpv/ai/LogicTechnique)





```mermaid
 classDiagram
    class LogicTechnique
    click LogicTechnique href "../LogicTechnique/"
      Technique <|-- LogicTechnique
        click Technique href "../Technique/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Technique](Technique.md)
        * **LogicTechnique**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:LogicTechnique](https://w3id.org/lmodel/dpv/ai/LogicTechnique) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Logic Technique




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#LogicTechnique |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:LogicTechnique |
| native | ai:LogicTechnique |
| exact | dpv_ai:LogicTechnique, dpv_ai_owl:LogicTechnique |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LogicTechnique
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LogicTechnique
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to logic based techniques
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Logic Technique
exact_mappings:
- dpv_ai:LogicTechnique
- dpv_ai_owl:LogicTechnique
is_a: Technique
class_uri: ai:LogicTechnique

```
</details>

### Induced

<details>
```yaml
name: LogicTechnique
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#LogicTechnique
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Refers to logic based techniques
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Logic Technique
exact_mappings:
- dpv_ai:LogicTechnique
- dpv_ai_owl:LogicTechnique
is_a: Technique
class_uri: ai:LogicTechnique

```
</details></div>