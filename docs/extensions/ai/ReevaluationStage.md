---
search:
  boost: 10.0
---

# Class: ReevaluationStage 


_The stage in the lifecycle where the AI system is reevaluated after the_

_operation and monitoring stage based on the operations of the AI system_



<div data-search-exclude markdown="1">



URI: [ai:ReevaluationStage](https://w3id.org/lmodel/dpv/ai/ReevaluationStage)





```mermaid
 classDiagram
    class ReevaluationStage
    click ReevaluationStage href "../ReevaluationStage/"
      LifecycleStage <|-- ReevaluationStage
        click LifecycleStage href "../LifecycleStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * **ReevaluationStage**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ReevaluationStage](https://w3id.org/lmodel/dpv/ai/ReevaluationStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Reevaluation Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ReevaluationStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ReevaluationStage |
| native | ai:ReevaluationStage |
| exact | dpv_ai:ReevaluationStage, dpv_ai_owl:ReevaluationStage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReevaluationStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ReevaluationStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is reevaluated after
  the

  operation and monitoring stage based on the operations of the AI system'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Reevaluation Stage
exact_mappings:
- dpv_ai:ReevaluationStage
- dpv_ai_owl:ReevaluationStage
is_a: LifecycleStage
class_uri: ai:ReevaluationStage

```
</details>

### Induced

<details>
```yaml
name: ReevaluationStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ReevaluationStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is reevaluated after
  the

  operation and monitoring stage based on the operations of the AI system'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Reevaluation Stage
exact_mappings:
- dpv_ai:ReevaluationStage
- dpv_ai_owl:ReevaluationStage
is_a: LifecycleStage
class_uri: ai:ReevaluationStage

```
</details></div>