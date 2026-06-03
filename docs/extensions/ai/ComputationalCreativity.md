---
search:
  boost: 10.0
---

# Class: ComputationalCreativity 


_computer systems that emulate human creative processes and produce_

_artistic, design output that simulates innovation and originality_



<div data-search-exclude markdown="1">



URI: [ai:ComputationalCreativity](https://w3id.org/lmodel/dpv/ai/ComputationalCreativity)





```mermaid
 classDiagram
    class ComputationalCreativity
    click ComputationalCreativity href "../ComputationalCreativity/"
      Capability <|-- ComputationalCreativity
        click Capability href "../Capability/"
      HumanOrientedCapability <|-- ComputationalCreativity
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * **ComputationalCreativity** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ComputationalCreativity](https://w3id.org/lmodel/dpv/ai/ComputationalCreativity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Computational Creativity




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ComputationalCreativity |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ComputationalCreativity |
| native | ai:ComputationalCreativity |
| exact | dpv_ai:ComputationalCreativity, dpv_ai_owl:ComputationalCreativity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ComputationalCreativity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ComputationalCreativity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'computer systems that emulate human creative processes and produce

  artistic, design output that simulates innovation and originality'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Computational Creativity
exact_mappings:
- dpv_ai:ComputationalCreativity
- dpv_ai_owl:ComputationalCreativity
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:ComputationalCreativity

```
</details>

### Induced

<details>
```yaml
name: ComputationalCreativity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ComputationalCreativity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'computer systems that emulate human creative processes and produce

  artistic, design output that simulates innovation and originality'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Computational Creativity
exact_mappings:
- dpv_ai:ComputationalCreativity
- dpv_ai_owl:ComputationalCreativity
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:ComputationalCreativity

```
</details></div>