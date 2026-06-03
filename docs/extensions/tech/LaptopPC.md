---
search:
  boost: 10.0
---

# Class: LaptopPC 


_A portal personal computer_



<div data-search-exclude markdown="1">



URI: [tech:LaptopPC](https://w3id.org/lmodel/dpv/tech/LaptopPC)





```mermaid
 classDiagram
    class LaptopPC
    click LaptopPC href "../LaptopPC/"
      PersonalComputer <|-- LaptopPC
        click PersonalComputer href "../PersonalComputer/"
      
      
```





## Inheritance
* **LaptopPC** [ [PersonalComputer](PersonalComputer.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:LaptopPC](https://w3id.org/lmodel/dpv/tech/LaptopPC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Laptop PC




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#LaptopPC |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:LaptopPC |
| native | tech:LaptopPC |
| exact | dpv_tech:LaptopPC, dpv_tech_owl:LaptopPC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LaptopPC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#LaptopPC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A portal personal computer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Laptop PC
exact_mappings:
- dpv_tech:LaptopPC
- dpv_tech_owl:LaptopPC
mixins:
- PersonalComputer
class_uri: tech:LaptopPC

```
</details>

### Induced

<details>
```yaml
name: LaptopPC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#LaptopPC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A portal personal computer
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Laptop PC
exact_mappings:
- dpv_tech:LaptopPC
- dpv_tech_owl:LaptopPC
mixins:
- PersonalComputer
class_uri: tech:LaptopPC

```
</details></div>