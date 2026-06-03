---
search:
  boost: 10.0
---

# Class: ReplaceStage 


_The stage in the lifecycle where the AI system is being replaced as part_

_of retirement_



<div data-search-exclude markdown="1">



URI: [ai:ReplaceStage](https://w3id.org/lmodel/dpv/ai/ReplaceStage)





```mermaid
 classDiagram
    class ReplaceStage
    click ReplaceStage href "../ReplaceStage/"
      LifecycleStage <|-- ReplaceStage
        click LifecycleStage href "../LifecycleStage/"
      RetirementStage <|-- ReplaceStage
        click RetirementStage href "../RetirementStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * [RetirementStage](RetirementStage.md)
        * **ReplaceStage** [ [LifecycleStage](LifecycleStage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ReplaceStage](https://w3id.org/lmodel/dpv/ai/ReplaceStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Replace Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ReplaceStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ReplaceStage |
| native | ai:ReplaceStage |
| exact | dpv_ai:ReplaceStage, dpv_ai_owl:ReplaceStage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReplaceStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ReplaceStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is being replaced as
  part

  of retirement'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Replace Stage
exact_mappings:
- dpv_ai:ReplaceStage
- dpv_ai_owl:ReplaceStage
is_a: RetirementStage
mixins:
- LifecycleStage
class_uri: ai:ReplaceStage

```
</details>

### Induced

<details>
```yaml
name: ReplaceStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ReplaceStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is being replaced as
  part

  of retirement'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Replace Stage
exact_mappings:
- dpv_ai:ReplaceStage
- dpv_ai_owl:ReplaceStage
is_a: RetirementStage
mixins:
- LifecycleStage
class_uri: ai:ReplaceStage

```
</details></div>