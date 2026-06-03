---
search:
  boost: 10.0
---

# Class: DesignStage 


_The stage in the lifecycle where designs are created for the AI system_



<div data-search-exclude markdown="1">



URI: [ai:DesignStage](https://w3id.org/lmodel/dpv/ai/DesignStage)





```mermaid
 classDiagram
    class DesignStage
    click DesignStage href "../DesignStage/"
      LifecycleStage <|-- DesignStage
        click LifecycleStage href "../LifecycleStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * **DesignStage**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DesignStage](https://w3id.org/lmodel/dpv/ai/DesignStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Design Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DesignStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DesignStage |
| native | ai:DesignStage |
| exact | dpv_ai:DesignStage, dpv_ai_owl:DesignStage |
| close | iso42001:AIReferenceControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DesignStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DesignStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: The stage in the lifecycle where designs are created for the AI system
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Design Stage
exact_mappings:
- dpv_ai:DesignStage
- dpv_ai_owl:DesignStage
close_mappings:
- iso42001:AIReferenceControl
is_a: LifecycleStage
class_uri: ai:DesignStage

```
</details>

### Induced

<details>
```yaml
name: DesignStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DesignStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: The stage in the lifecycle where designs are created for the AI system
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Design Stage
exact_mappings:
- dpv_ai:DesignStage
- dpv_ai_owl:DesignStage
close_mappings:
- iso42001:AIReferenceControl
is_a: LifecycleStage
class_uri: ai:DesignStage

```
</details></div>