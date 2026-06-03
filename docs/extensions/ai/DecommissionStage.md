---
search:
  boost: 10.0
---

# Class: DecommissionStage 


_The stage in the lifecycle where the AI system is being decommissioned_

_as part of retirement_



<div data-search-exclude markdown="1">



URI: [ai:DecommissionStage](https://w3id.org/lmodel/dpv/ai/DecommissionStage)





```mermaid
 classDiagram
    class DecommissionStage
    click DecommissionStage href "../DecommissionStage/"
      LifecycleStage <|-- DecommissionStage
        click LifecycleStage href "../LifecycleStage/"
      RetirementStage <|-- DecommissionStage
        click RetirementStage href "../RetirementStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * [RetirementStage](RetirementStage.md)
        * **DecommissionStage** [ [LifecycleStage](LifecycleStage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DecommissionStage](https://w3id.org/lmodel/dpv/ai/DecommissionStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Decommission Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DecommissionStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DecommissionStage |
| native | ai:DecommissionStage |
| exact | dpv_ai:DecommissionStage, dpv_ai_owl:DecommissionStage |
| close | iso42001:AIReferenceControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DecommissionStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DecommissionStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is being decommissioned

  as part of retirement'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Decommission Stage
exact_mappings:
- dpv_ai:DecommissionStage
- dpv_ai_owl:DecommissionStage
close_mappings:
- iso42001:AIReferenceControl
is_a: RetirementStage
mixins:
- LifecycleStage
class_uri: ai:DecommissionStage

```
</details>

### Induced

<details>
```yaml
name: DecommissionStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DecommissionStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is being decommissioned

  as part of retirement'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Decommission Stage
exact_mappings:
- dpv_ai:DecommissionStage
- dpv_ai_owl:DecommissionStage
close_mappings:
- iso42001:AIReferenceControl
is_a: RetirementStage
mixins:
- LifecycleStage
class_uri: ai:DecommissionStage

```
</details></div>