---
search:
  boost: 10.0
---

# Class: Manufacturer 


_Actor that manufactures Technology_



<div data-search-exclude markdown="1">



URI: [tech:Manufacturer](https://w3id.org/lmodel/dpv/tech/Manufacturer)





```mermaid
 classDiagram
    class Manufacturer
    click Manufacturer href "../Manufacturer/"
      Actor <|-- Manufacturer
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **Manufacturer**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Manufacturer](https://w3id.org/lmodel/dpv/tech/Manufacturer) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Manufacturer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | DGA 26.3 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Manufacturer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Manufacturer |
| native | tech:Manufacturer |
| exact | dpv_tech:Manufacturer, dpv_tech_owl:Manufacturer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Manufacturer
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Manufacturer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that manufactures Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Manufacturer
exact_mappings:
- dpv_tech:Manufacturer
- dpv_tech_owl:Manufacturer
is_a: Actor
class_uri: tech:Manufacturer

```
</details>

### Induced

<details>
```yaml
name: Manufacturer
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Manufacturer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that manufactures Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Manufacturer
exact_mappings:
- dpv_tech:Manufacturer
- dpv_tech_owl:Manufacturer
is_a: Actor
class_uri: tech:Manufacturer

```
</details></div>