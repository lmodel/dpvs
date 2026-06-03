---
search:
  boost: 10.0
---

# Class: VerificationStage 


_The stage in the lifecycle where the AI system is being verified to_

_satisfy requirements and meet objectives_



<div data-search-exclude markdown="1">



URI: [ai:VerificationStage](https://w3id.org/lmodel/dpv/ai/VerificationStage)





```mermaid
 classDiagram
    class VerificationStage
    click VerificationStage href "../VerificationStage/"
      LifecycleStage <|-- VerificationStage
        click LifecycleStage href "../LifecycleStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * **VerificationStage**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:VerificationStage](https://w3id.org/lmodel/dpv/ai/VerificationStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Verification Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#VerificationStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:VerificationStage |
| native | ai:VerificationStage |
| exact | dpv_ai:VerificationStage, dpv_ai_owl:VerificationStage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VerificationStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#VerificationStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is being verified to

  satisfy requirements and meet objectives'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Verification Stage
exact_mappings:
- dpv_ai:VerificationStage
- dpv_ai_owl:VerificationStage
is_a: LifecycleStage
class_uri: ai:VerificationStage

```
</details>

### Induced

<details>
```yaml
name: VerificationStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#VerificationStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is being verified to

  satisfy requirements and meet objectives'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Verification Stage
exact_mappings:
- dpv_ai:VerificationStage
- dpv_ai_owl:VerificationStage
is_a: LifecycleStage
class_uri: ai:VerificationStage

```
</details></div>