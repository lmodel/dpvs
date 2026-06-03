---
search:
  boost: 10.0
---

# Class: ServiceRobot 


_A robot or robotic system in personal use or professional use that_

_performs useful tasks for humans or equipment_



<div data-search-exclude markdown="1">



URI: [ai:ServiceRobot](https://w3id.org/lmodel/dpv/ai/ServiceRobot)





```mermaid
 classDiagram
    class ServiceRobot
    click ServiceRobot href "../ServiceRobot/"
      Robot <|-- ServiceRobot
        click Robot href "../Robot/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [AISystem](AISystem.md)
        * [Robot](Robot.md)
            * **ServiceRobot**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ServiceRobot](https://w3id.org/lmodel/dpv/ai/ServiceRobot) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Service Robot




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source |  ISO 8373:2021 3.7 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ServiceRobot |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ServiceRobot |
| native | ai:ServiceRobot |
| exact | dpv_ai:ServiceRobot, dpv_ai_owl:ServiceRobot |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceRobot
annotations:
  dct_source:
    tag: dct_source
    value: ' ISO 8373:2021 3.7'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ServiceRobot
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'A robot or robotic system in personal use or professional use that

  performs useful tasks for humans or equipment'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Service Robot
exact_mappings:
- dpv_ai:ServiceRobot
- dpv_ai_owl:ServiceRobot
is_a: Robot
class_uri: ai:ServiceRobot

```
</details>

### Induced

<details>
```yaml
name: ServiceRobot
annotations:
  dct_source:
    tag: dct_source
    value: ' ISO 8373:2021 3.7'
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ServiceRobot
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'A robot or robotic system in personal use or professional use that

  performs useful tasks for humans or equipment'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Service Robot
exact_mappings:
- dpv_ai:ServiceRobot
- dpv_ai_owl:ServiceRobot
is_a: Robot
class_uri: ai:ServiceRobot

```
</details></div>