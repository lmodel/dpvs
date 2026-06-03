---
search:
  boost: 10.0
---

# Class: Telephone 


_Telephone_



<div data-search-exclude markdown="1">



URI: [tech:Telephone](https://w3id.org/lmodel/dpv/tech/Telephone)





```mermaid
 classDiagram
    class Telephone
    click Telephone href "../Telephone/"
      Device <|-- Telephone
        click Device href "../Device/"
      

      Telephone <|-- MobilePhone
        click MobilePhone href "../MobilePhone/"
      

      
```





## Inheritance
* [Device](Device.md) [ [Hardware](Hardware.md)]
    * **Telephone**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Telephone](https://w3id.org/lmodel/dpv/tech/Telephone) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Telephone




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Telephone |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Telephone |
| native | tech:Telephone |
| exact | dpv_tech:Telephone, dpv_tech_owl:Telephone |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Telephone
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Telephone
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Telephone
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Telephone
exact_mappings:
- dpv_tech:Telephone
- dpv_tech_owl:Telephone
is_a: Device
class_uri: tech:Telephone

```
</details>

### Induced

<details>
```yaml
name: Telephone
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Telephone
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Telephone
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Telephone
exact_mappings:
- dpv_tech:Telephone
- dpv_tech_owl:Telephone
is_a: Device
class_uri: tech:Telephone

```
</details></div>