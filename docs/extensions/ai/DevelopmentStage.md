---
search:
  boost: 10.0
---

# Class: DevelopmentStage 


_The stage in the lifecycle where the development and creation of the_

_system occurs, signalling upon completion that it is ready for_

_verification and validation_



<div data-search-exclude markdown="1">



URI: [ai:DevelopmentStage](https://w3id.org/lmodel/dpv/ai/DevelopmentStage)





```mermaid
 classDiagram
    class DevelopmentStage
    click DevelopmentStage href "../DevelopmentStage/"
      LifecycleStage <|-- DevelopmentStage
        click LifecycleStage href "../LifecycleStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * **DevelopmentStage**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DevelopmentStage](https://w3id.org/lmodel/dpv/ai/DevelopmentStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Development Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DevelopmentStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DevelopmentStage |
| native | ai:DevelopmentStage |
| exact | dpv_ai:DevelopmentStage, dpv_ai_owl:DevelopmentStage |
| close | iso42001:AIReferenceControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DevelopmentStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DevelopmentStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the development and creation of the

  system occurs, signalling upon completion that it is ready for

  verification and validation'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Development Stage
exact_mappings:
- dpv_ai:DevelopmentStage
- dpv_ai_owl:DevelopmentStage
close_mappings:
- iso42001:AIReferenceControl
is_a: LifecycleStage
class_uri: ai:DevelopmentStage

```
</details>

### Induced

<details>
```yaml
name: DevelopmentStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DevelopmentStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the development and creation of the

  system occurs, signalling upon completion that it is ready for

  verification and validation'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Development Stage
exact_mappings:
- dpv_ai:DevelopmentStage
- dpv_ai_owl:DevelopmentStage
close_mappings:
- iso42001:AIReferenceControl
is_a: LifecycleStage
class_uri: ai:DevelopmentStage

```
</details></div>