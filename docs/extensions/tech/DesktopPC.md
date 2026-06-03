---
search:
  boost: 10.0
---

# Class: DesktopPC 


_A non-portable or fixed personal computer_



<div data-search-exclude markdown="1">



URI: [tech:DesktopPC](https://w3id.org/lmodel/dpv/tech/DesktopPC)





```mermaid
 classDiagram
    class DesktopPC
    click DesktopPC href "../DesktopPC/"
      PersonalComputer <|-- DesktopPC
        click PersonalComputer href "../PersonalComputer/"
      
      
```





## Inheritance
* **DesktopPC** [ [PersonalComputer](PersonalComputer.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:DesktopPC](https://w3id.org/lmodel/dpv/tech/DesktopPC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Desktop PC




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#DesktopPC |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:DesktopPC |
| native | tech:DesktopPC |
| exact | dpv_tech:DesktopPC, dpv_tech_owl:DesktopPC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DesktopPC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#DesktopPC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A non-portable or fixed personal computer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Desktop PC
exact_mappings:
- dpv_tech:DesktopPC
- dpv_tech_owl:DesktopPC
mixins:
- PersonalComputer
class_uri: tech:DesktopPC

```
</details>

### Induced

<details>
```yaml
name: DesktopPC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#DesktopPC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A non-portable or fixed personal computer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Desktop PC
exact_mappings:
- dpv_tech:DesktopPC
- dpv_tech_owl:DesktopPC
mixins:
- PersonalComputer
class_uri: tech:DesktopPC

```
</details></div>