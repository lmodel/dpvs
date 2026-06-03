---
search:
  boost: 10.0
---

# Class: RepairStage 


_The stage in the lifecycle where an AI system is being repaired due to_

_suspected or occurred incidents_



<div data-search-exclude markdown="1">



URI: [ai:RepairStage](https://w3id.org/lmodel/dpv/ai/RepairStage)





```mermaid
 classDiagram
    class RepairStage
    click RepairStage href "../RepairStage/"
      LifecycleStage <|-- RepairStage
        click LifecycleStage href "../LifecycleStage/"
      OperationStage <|-- RepairStage
        click OperationStage href "../OperationStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * [OperationStage](OperationStage.md)
        * **RepairStage** [ [LifecycleStage](LifecycleStage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:RepairStage](https://w3id.org/lmodel/dpv/ai/RepairStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Repair Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#RepairStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:RepairStage |
| native | ai:RepairStage |
| exact | dpv_ai:RepairStage, dpv_ai_owl:RepairStage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RepairStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RepairStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where an AI system is being repaired due
  to

  suspected or occurred incidents'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Repair Stage
exact_mappings:
- dpv_ai:RepairStage
- dpv_ai_owl:RepairStage
is_a: OperationStage
mixins:
- LifecycleStage
class_uri: ai:RepairStage

```
</details>

### Induced

<details>
```yaml
name: RepairStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#RepairStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where an AI system is being repaired due
  to

  suspected or occurred incidents'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Repair Stage
exact_mappings:
- dpv_ai:RepairStage
- dpv_ai_owl:RepairStage
is_a: OperationStage
mixins:
- LifecycleStage
class_uri: ai:RepairStage

```
</details></div>