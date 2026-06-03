---
search:
  boost: 10.0
---

# Class: SocialRobot 


_A robot or robotic system with social interaction functions_



<div data-search-exclude markdown="1">



URI: [ai:SocialRobot](https://w3id.org/lmodel/dpv/ai/SocialRobot)





```mermaid
 classDiagram
    class SocialRobot
    click SocialRobot href "../SocialRobot/"
      Robot <|-- SocialRobot
        click Robot href "../Robot/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [AISystem](AISystem.md)
        * [Robot](Robot.md)
            * **SocialRobot**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:SocialRobot](https://w3id.org/lmodel/dpv/ai/SocialRobot) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Social Robot




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  Defining Artificial Intelligence 2.0 |
| upstream_iri | https://w3id.org/dpv/ai/owl#SocialRobot |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:SocialRobot |
| native | ai:SocialRobot |
| exact | dpv_ai:SocialRobot, dpv_ai_owl:SocialRobot |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SocialRobot
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SocialRobot
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: A robot or robotic system with social interaction functions
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Social Robot
exact_mappings:
- dpv_ai:SocialRobot
- dpv_ai_owl:SocialRobot
is_a: Robot
class_uri: ai:SocialRobot

```
</details>

### Induced

<details>
```yaml
name: SocialRobot
annotations:
  dct_source:
    tag: dct_source
    value: ' Defining Artificial Intelligence 2.0'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#SocialRobot
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: A robot or robotic system with social interaction functions
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Social Robot
exact_mappings:
- dpv_ai:SocialRobot
- dpv_ai_owl:SocialRobot
is_a: Robot
class_uri: ai:SocialRobot

```
</details></div>