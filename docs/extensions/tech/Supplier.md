---
search:
  boost: 10.0
---

# Class: Supplier 


_Actor that supplies Technology_



<div data-search-exclude markdown="1">



URI: [tech:Supplier](https://w3id.org/lmodel/dpv/tech/Supplier)





```mermaid
 classDiagram
    class Supplier
    click Supplier href "../Supplier/"
      Actor <|-- Supplier
        click Actor href "../Actor/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * **Supplier**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Supplier](https://w3id.org/lmodel/dpv/tech/Supplier) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Supplier




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | DGA 26.3 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Supplier |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Supplier |
| native | tech:Supplier |
| exact | dpv_tech:Supplier, dpv_tech_owl:Supplier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Supplier
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Supplier
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that supplies Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Supplier
exact_mappings:
- dpv_tech:Supplier
- dpv_tech_owl:Supplier
is_a: Actor
class_uri: tech:Supplier

```
</details>

### Induced

<details>
```yaml
name: Supplier
annotations:
  dct_source:
    tag: dct_source
    value: DGA 26.3
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Supplier
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that supplies Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Supplier
exact_mappings:
- dpv_tech:Supplier
- dpv_tech_owl:Supplier
is_a: Actor
class_uri: tech:Supplier

```
</details></div>