---
search:
  boost: 10.0
---

# Class: ValidationStage 


_The stage in the lifecycle where the AI system is validated for_

_requirements and objectives for an intended use or application_



<div data-search-exclude markdown="1">



URI: [ai:ValidationStage](https://w3id.org/lmodel/dpv/ai/ValidationStage)





```mermaid
 classDiagram
    class ValidationStage
    click ValidationStage href "../ValidationStage/"
      LifecycleStage <|-- ValidationStage
        click LifecycleStage href "../LifecycleStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * **ValidationStage**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationStage](https://w3id.org/lmodel/dpv/ai/ValidationStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationStage |
| native | ai:ValidationStage |
| exact | dpv_ai:ValidationStage, dpv_ai_owl:ValidationStage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is validated for

  requirements and objectives for an intended use or application'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Stage
exact_mappings:
- dpv_ai:ValidationStage
- dpv_ai_owl:ValidationStage
is_a: LifecycleStage
class_uri: ai:ValidationStage

```
</details>

### Induced

<details>
```yaml
name: ValidationStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is validated for

  requirements and objectives for an intended use or application'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Stage
exact_mappings:
- dpv_ai:ValidationStage
- dpv_ai_owl:ValidationStage
is_a: LifecycleStage
class_uri: ai:ValidationStage

```
</details></div>