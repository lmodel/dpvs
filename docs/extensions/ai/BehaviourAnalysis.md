---
search:
  boost: 10.0
---

# Class: BehaviourAnalysis 


_Capability of a system in analysing people's behaviour_



<div data-search-exclude markdown="1">



URI: [ai:BehaviourAnalysis](https://w3id.org/lmodel/dpv/ai/BehaviourAnalysis)





```mermaid
 classDiagram
    class BehaviourAnalysis
    click BehaviourAnalysis href "../BehaviourAnalysis/"
      Capability <|-- BehaviourAnalysis
        click Capability href "../Capability/"
      HumanOrientedCapability <|-- BehaviourAnalysis
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * **BehaviourAnalysis** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BehaviourAnalysis](https://w3id.org/lmodel/dpv/ai/BehaviourAnalysis) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Behaviour Analysis




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BehaviourAnalysis |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BehaviourAnalysis |
| native | ai:BehaviourAnalysis |
| exact | dpv_ai:BehaviourAnalysis, dpv_ai_owl:BehaviourAnalysis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BehaviourAnalysis
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BehaviourAnalysis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability of a system in analysing people's behaviour
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Behaviour Analysis
exact_mappings:
- dpv_ai:BehaviourAnalysis
- dpv_ai_owl:BehaviourAnalysis
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:BehaviourAnalysis

```
</details>

### Induced

<details>
```yaml
name: BehaviourAnalysis
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BehaviourAnalysis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability of a system in analysing people's behaviour
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Behaviour Analysis
exact_mappings:
- dpv_ai:BehaviourAnalysis
- dpv_ai_owl:BehaviourAnalysis
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:BehaviourAnalysis

```
</details></div>