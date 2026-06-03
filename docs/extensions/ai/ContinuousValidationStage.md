---
search:
  boost: 10.0
---

# Class: ContinuousValidationStage 


_The stage in the lifecycle where there is continuous learning within the_

_AI system by incremental training on an ongoing basis while the system_

_is running in production_



<div data-search-exclude markdown="1">



URI: [ai:ContinuousValidationStage](https://w3id.org/lmodel/dpv/ai/ContinuousValidationStage)





```mermaid
 classDiagram
    class ContinuousValidationStage
    click ContinuousValidationStage href "../ContinuousValidationStage/"
      LifecycleStage <|-- ContinuousValidationStage
        click LifecycleStage href "../LifecycleStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * **ContinuousValidationStage**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ContinuousValidationStage](https://w3id.org/lmodel/dpv/ai/ContinuousValidationStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Continuous Validation Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ContinuousValidationStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ContinuousValidationStage |
| native | ai:ContinuousValidationStage |
| exact | dpv_ai:ContinuousValidationStage, dpv_ai_owl:ContinuousValidationStage |
| close | iso42001:AIReferenceControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContinuousValidationStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ContinuousValidationStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where there is continuous learning within
  the

  AI system by incremental training on an ongoing basis while the system

  is running in production'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Continuous Validation Stage
exact_mappings:
- dpv_ai:ContinuousValidationStage
- dpv_ai_owl:ContinuousValidationStage
close_mappings:
- iso42001:AIReferenceControl
is_a: LifecycleStage
class_uri: ai:ContinuousValidationStage

```
</details>

### Induced

<details>
```yaml
name: ContinuousValidationStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ContinuousValidationStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where there is continuous learning within
  the

  AI system by incremental training on an ongoing basis while the system

  is running in production'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Continuous Validation Stage
exact_mappings:
- dpv_ai:ContinuousValidationStage
- dpv_ai_owl:ContinuousValidationStage
close_mappings:
- iso42001:AIReferenceControl
is_a: LifecycleStage
class_uri: ai:ContinuousValidationStage

```
</details></div>