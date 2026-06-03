---
search:
  boost: 10.0
---

# Class: IndustrialRobot 


_A robot or robotic system for use in industrial automation applications_



<div data-search-exclude markdown="1">



URI: [ai:IndustrialRobot](https://w3id.org/lmodel/dpv/ai/IndustrialRobot)





```mermaid
 classDiagram
    class IndustrialRobot
    click IndustrialRobot href "../IndustrialRobot/"
      Robot <|-- IndustrialRobot
        click Robot href "../Robot/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [AISystem](AISystem.md)
        * [Robot](Robot.md)
            * **IndustrialRobot**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:IndustrialRobot](https://w3id.org/lmodel/dpv/ai/IndustrialRobot) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Industrial Robot




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.1.29 |
| upstream_iri | https://w3id.org/dpv/ai/owl#IndustrialRobot |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:IndustrialRobot |
| native | ai:IndustrialRobot |
| exact | dpv_ai:IndustrialRobot, dpv_ai_owl:IndustrialRobot |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IndustrialRobot
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.1.29
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#IndustrialRobot
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: A robot or robotic system for use in industrial automation applications
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Industrial Robot
exact_mappings:
- dpv_ai:IndustrialRobot
- dpv_ai_owl:IndustrialRobot
is_a: Robot
class_uri: ai:IndustrialRobot

```
</details>

### Induced

<details>
```yaml
name: IndustrialRobot
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.1.29
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#IndustrialRobot
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: A robot or robotic system for use in industrial automation applications
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Industrial Robot
exact_mappings:
- dpv_ai:IndustrialRobot
- dpv_ai_owl:IndustrialRobot
is_a: Robot
class_uri: ai:IndustrialRobot

```
</details></div>