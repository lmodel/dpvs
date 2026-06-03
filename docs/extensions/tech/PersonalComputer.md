---
search:
  boost: 10.0
---

# Class: PersonalComputer 


_A computing device intended for individual use_



<div data-search-exclude markdown="1">



URI: [tech:PersonalComputer](https://w3id.org/lmodel/dpv/tech/PersonalComputer)





```mermaid
 classDiagram
    class PersonalComputer
    click PersonalComputer href "../PersonalComputer/"
      Device <|-- PersonalComputer
        click Device href "../Device/"
      

      PersonalComputer <|-- DesktopPC
        click DesktopPC href "../DesktopPC/"
      PersonalComputer <|-- LaptopPC
        click LaptopPC href "../LaptopPC/"
      PersonalComputer <|-- Smartphone
        click Smartphone href "../Smartphone/"
      

      
```





## Inheritance
* **PersonalComputer** [ [Device](Device.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:PersonalComputer](https://w3id.org/lmodel/dpv/tech/PersonalComputer) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Personal Computer (PC)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#PersonalComputer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:PersonalComputer |
| native | tech:PersonalComputer |
| exact | dpv_tech:PersonalComputer, dpv_tech_owl:PersonalComputer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonalComputer
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#PersonalComputer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A computing device intended for individual use
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Personal Computer (PC)
exact_mappings:
- dpv_tech:PersonalComputer
- dpv_tech_owl:PersonalComputer
mixins:
- Device
class_uri: tech:PersonalComputer

```
</details>

### Induced

<details>
```yaml
name: PersonalComputer
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#PersonalComputer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A computing device intended for individual use
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Personal Computer (PC)
exact_mappings:
- dpv_tech:PersonalComputer
- dpv_tech_owl:PersonalComputer
mixins:
- Device
class_uri: tech:PersonalComputer

```
</details></div>