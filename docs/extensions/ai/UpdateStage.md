---
search:
  boost: 10.0
---

# Class: UpdateStage 


_The stage in the lifecycle where an AI system is being or has been_

_updated_



<div data-search-exclude markdown="1">



URI: [ai:UpdateStage](https://w3id.org/lmodel/dpv/ai/UpdateStage)





```mermaid
 classDiagram
    class UpdateStage
    click UpdateStage href "../UpdateStage/"
      LifecycleStage <|-- UpdateStage
        click LifecycleStage href "../LifecycleStage/"
      OperationStage <|-- UpdateStage
        click OperationStage href "../OperationStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * [OperationStage](OperationStage.md)
        * **UpdateStage** [ [LifecycleStage](LifecycleStage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:UpdateStage](https://w3id.org/lmodel/dpv/ai/UpdateStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Update Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#UpdateStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:UpdateStage |
| native | ai:UpdateStage |
| exact | dpv_ai:UpdateStage, dpv_ai_owl:UpdateStage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UpdateStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#UpdateStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where an AI system is being or has been

  updated'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Update Stage
exact_mappings:
- dpv_ai:UpdateStage
- dpv_ai_owl:UpdateStage
is_a: OperationStage
mixins:
- LifecycleStage
class_uri: ai:UpdateStage

```
</details>

### Induced

<details>
```yaml
name: UpdateStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#UpdateStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where an AI system is being or has been

  updated'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Update Stage
exact_mappings:
- dpv_ai:UpdateStage
- dpv_ai_owl:UpdateStage
is_a: OperationStage
mixins:
- LifecycleStage
class_uri: ai:UpdateStage

```
</details></div>