---
search:
  boost: 10.0
---

# Class: PersonalityTraitAnalysis 


_Capability for determining and analysing people's personality traits_



<div data-search-exclude markdown="1">



URI: [ai:PersonalityTraitAnalysis](https://w3id.org/lmodel/dpv/ai/PersonalityTraitAnalysis)





```mermaid
 classDiagram
    class PersonalityTraitAnalysis
    click PersonalityTraitAnalysis href "../PersonalityTraitAnalysis/"
      Capability <|-- PersonalityTraitAnalysis
        click Capability href "../Capability/"
      HumanOrientedCapability <|-- PersonalityTraitAnalysis
        click HumanOrientedCapability href "../HumanOrientedCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * **PersonalityTraitAnalysis** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:PersonalityTraitAnalysis](https://w3id.org/lmodel/dpv/ai/PersonalityTraitAnalysis) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Personality Trait Analysis




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#PersonalityTraitAnalysis |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:PersonalityTraitAnalysis |
| native | ai:PersonalityTraitAnalysis |
| exact | dpv_ai:PersonalityTraitAnalysis, dpv_ai_owl:PersonalityTraitAnalysis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonalityTraitAnalysis
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#PersonalityTraitAnalysis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for determining and analysing people's personality traits
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Personality Trait Analysis
exact_mappings:
- dpv_ai:PersonalityTraitAnalysis
- dpv_ai_owl:PersonalityTraitAnalysis
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:PersonalityTraitAnalysis

```
</details>

### Induced

<details>
```yaml
name: PersonalityTraitAnalysis
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#PersonalityTraitAnalysis
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Capability for determining and analysing people's personality traits
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Personality Trait Analysis
exact_mappings:
- dpv_ai:PersonalityTraitAnalysis
- dpv_ai_owl:PersonalityTraitAnalysis
is_a: HumanOrientedCapability
mixins:
- Capability
class_uri: ai:PersonalityTraitAnalysis

```
</details></div>