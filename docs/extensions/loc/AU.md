---
search:
  boost: 10.0
---

# Class: AU 


_Concept representing Country of Australia_



<div data-search-exclude markdown="1">



URI: [loc:AU](https://w3id.org/lmodel/dpv/loc/AU)





```mermaid
 classDiagram
    class AU
    click AU href "../AU/"
      AU <|-- AUACT
        click AUACT href "../AUACT/"
      AU <|-- AUNSW
        click AUNSW href "../AUNSW/"
      AU <|-- AUNT
        click AUNT href "../AUNT/"
      AU <|-- AUQLD
        click AUQLD href "../AUQLD/"
      AU <|-- AUSA
        click AUSA href "../AUSA/"
      AU <|-- AUTAS
        click AUTAS href "../AUTAS/"
      AU <|-- AUVIC
        click AUVIC href "../AUVIC/"
      AU <|-- AUWA
        click AUWA href "../AUWA/"
      
      
```





## Inheritance
* **AU**
    * [AUACT](AUACT.md)
    * [AUNSW](AUNSW.md)
    * [AUNT](AUNT.md)
    * [AUQLD](AUQLD.md)
    * [AUSA](AUSA.md)
    * [AUTAS](AUTAS.md)
    * [AUVIC](AUVIC.md)
    * [AUWA](AUWA.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AU](https://w3id.org/lmodel/dpv/loc/AU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Australia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AU |
| native | loc:AU |
| exact | dpv_loc:AU, dpv_loc_owl:AU, iso3166:AU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Australia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Australia
exact_mappings:
- dpv_loc:AU
- dpv_loc_owl:AU
- iso3166:AU
class_uri: loc:AU

```
</details>

### Induced

<details>
```yaml
name: AU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Australia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Australia
exact_mappings:
- dpv_loc:AU
- dpv_loc_owl:AU
- iso3166:AU
class_uri: loc:AU

```
</details></div>