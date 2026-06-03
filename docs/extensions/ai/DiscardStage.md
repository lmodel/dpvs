---
search:
  boost: 10.0
---

# Class: DiscardStage 


_The stage in the lifecycle where the AI system is being discarded as_

_part of retirement_



<div data-search-exclude markdown="1">



URI: [ai:DiscardStage](https://w3id.org/lmodel/dpv/ai/DiscardStage)





```mermaid
 classDiagram
    class DiscardStage
    click DiscardStage href "../DiscardStage/"
      LifecycleStage <|-- DiscardStage
        click LifecycleStage href "../LifecycleStage/"
      RetirementStage <|-- DiscardStage
        click RetirementStage href "../RetirementStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * [RetirementStage](RetirementStage.md)
        * **DiscardStage** [ [LifecycleStage](LifecycleStage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DiscardStage](https://w3id.org/lmodel/dpv/ai/DiscardStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Discard Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DiscardStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DiscardStage |
| native | ai:DiscardStage |
| exact | dpv_ai:DiscardStage, dpv_ai_owl:DiscardStage |
| close | iso42001:AIReferenceControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DiscardStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DiscardStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is being discarded as

  part of retirement'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Discard Stage
exact_mappings:
- dpv_ai:DiscardStage
- dpv_ai_owl:DiscardStage
close_mappings:
- iso42001:AIReferenceControl
is_a: RetirementStage
mixins:
- LifecycleStage
class_uri: ai:DiscardStage

```
</details>

### Induced

<details>
```yaml
name: DiscardStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DiscardStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is being discarded as

  part of retirement'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Discard Stage
exact_mappings:
- dpv_ai:DiscardStage
- dpv_ai_owl:DiscardStage
close_mappings:
- iso42001:AIReferenceControl
is_a: RetirementStage
mixins:
- LifecycleStage
class_uri: ai:DiscardStage

```
</details></div>