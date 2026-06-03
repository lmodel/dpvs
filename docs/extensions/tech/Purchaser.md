---
search:
  boost: 10.0
---

# Class: Purchaser 


_Actor that purchases Technology_



<div data-search-exclude markdown="1">



URI: [tech:Purchaser](https://w3id.org/lmodel/dpv/tech/Purchaser)





```mermaid
 classDiagram
    class Purchaser
    click Purchaser href "../Purchaser/"
      Actor <|-- Purchaser
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **Purchaser**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Purchaser](https://w3id.org/lmodel/dpv/tech/Purchaser) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Purchaser




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | DGA 26.3 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Purchaser |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Purchaser |
| native | tech:Purchaser |
| exact | dpv_tech:Purchaser, dpv_tech_owl:Purchaser |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Purchaser
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Purchaser
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that purchases Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Purchaser
exact_mappings:
- dpv_tech:Purchaser
- dpv_tech_owl:Purchaser
is_a: Actor
class_uri: tech:Purchaser

```
</details>

### Induced

<details>
```yaml
name: Purchaser
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Purchaser
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that purchases Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Purchaser
exact_mappings:
- dpv_tech:Purchaser
- dpv_tech_owl:Purchaser
is_a: Actor
class_uri: tech:Purchaser

```
</details></div>