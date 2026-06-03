---
search:
  boost: 10.0
---

# Class: Robot 


_An automation system with actuators that performs intended tasks in the_

_physical world, by means of sensing its environment and a software_

_control system_



<div data-search-exclude markdown="1">



URI: [ai:Robot](https://w3id.org/lmodel/dpv/ai/Robot)





```mermaid
 classDiagram
    class Robot
    click Robot href "../Robot/"
      AISystem <|-- Robot
        click AISystem href "../AISystem/"
      

      Robot <|-- IndustrialRobot
        click IndustrialRobot href "../IndustrialRobot/"
      Robot <|-- ServiceRobot
        click ServiceRobot href "../ServiceRobot/"
      Robot <|-- SocialRobot
        click SocialRobot href "../SocialRobot/"
      

      
```





## Inheritance
* [AI](AI.md)
    * [AISystem](AISystem.md)
        * **Robot**
            * [IndustrialRobot](IndustrialRobot.md)
            * [ServiceRobot](ServiceRobot.md)
            * [SocialRobot](SocialRobot.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:Robot](https://w3id.org/lmodel/dpv/ai/Robot) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Robot




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 3.1.29 |
| upstream_iri | https://w3id.org/dpv/ai/owl#Robot |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:Robot |
| native | ai:Robot |
| exact | dpv_ai:Robot, dpv_ai_owl:Robot |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Robot
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.1.29
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#Robot
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'An automation system with actuators that performs intended tasks in
  the

  physical world, by means of sensing its environment and a software

  control system'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Robot
exact_mappings:
- dpv_ai:Robot
- dpv_ai_owl:Robot
is_a: AISystem
class_uri: ai:Robot

```
</details>

### Induced

<details>
```yaml
name: Robot
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022 3.1.29
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#Robot
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'An automation system with actuators that performs intended tasks in
  the

  physical world, by means of sensing its environment and a software

  control system'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Robot
exact_mappings:
- dpv_ai:Robot
- dpv_ai_owl:Robot
is_a: AISystem
class_uri: ai:Robot

```
</details></div>