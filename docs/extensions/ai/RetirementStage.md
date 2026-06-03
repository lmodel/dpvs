---
search:
  boost: 10.0
---

# Class: RetirementStage 


_The stage in the lifecycle where the AI system is retired and becomes_

_obsolete_



<div data-search-exclude markdown="1">



URI: [ai:RetirementStage](https://w3id.org/lmodel/dpv/ai/RetirementStage)





```mermaid
 classDiagram
    class RetirementStage
    click RetirementStage href "../RetirementStage/"
      LifecycleStage <|-- RetirementStage
        click LifecycleStage href "../LifecycleStage/"
      

      RetirementStage <|-- DecommissionStage
        click DecommissionStage href "../DecommissionStage/"
      RetirementStage <|-- DiscardStage
        click DiscardStage href "../DiscardStage/"
      RetirementStage <|-- ReplaceStage
        click ReplaceStage href "../ReplaceStage/"
      

      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * **RetirementStage**
        * [DecommissionStage](DecommissionStage.md) [ [LifecycleStage](LifecycleStage.md)]
        * [DiscardStage](DiscardStage.md) [ [LifecycleStage](LifecycleStage.md)]
        * [ReplaceStage](ReplaceStage.md) [ [LifecycleStage](LifecycleStage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:RetirementStage](https://w3id.org/lmodel/dpv/ai/RetirementStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Retirement Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#RetirementStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:RetirementStage |
| native | ai:RetirementStage |
| exact | dpv_ai:RetirementStage, dpv_ai_owl:RetirementStage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RetirementStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RetirementStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is retired and becomes

  obsolete'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Retirement Stage
exact_mappings:
- dpv_ai:RetirementStage
- dpv_ai_owl:RetirementStage
is_a: LifecycleStage
class_uri: ai:RetirementStage

```
</details>

### Induced

<details>
```yaml
name: RetirementStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RetirementStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is retired and becomes

  obsolete'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Retirement Stage
exact_mappings:
- dpv_ai:RetirementStage
- dpv_ai_owl:RetirementStage
is_a: LifecycleStage
class_uri: ai:RetirementStage

```
</details></div>