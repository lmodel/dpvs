---
search:
  boost: 10.0
---

# Class: VU 


_Concept representing Country of Vanuatu_



<div data-search-exclude markdown="1">



URI: [loc:VU](https://w3id.org/lmodel/dpv/loc/VU)





```mermaid
 classDiagram
    class VU
    click VU href "../VU/"
      VU <|-- VUPAM
        click VUPAM href "../VUPAM/"
      VU <|-- VUSAM
        click VUSAM href "../VUSAM/"
      VU <|-- VUTAE
        click VUTAE href "../VUTAE/"
      VU <|-- VUTOB
        click VUTOB href "../VUTOB/"
      
      
```





## Inheritance
* **VU**
    * [VUPAM](VUPAM.md)
    * [VUSAM](VUSAM.md)
    * [VUTAE](VUTAE.md)
    * [VUTOB](VUTOB.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:VU](https://w3id.org/lmodel/dpv/loc/VU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Vanuatu




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#VU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:VU |
| native | loc:VU |
| exact | dpv_loc:VU, dpv_loc_owl:VU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Vanuatu
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Vanuatu
exact_mappings:
- dpv_loc:VU
- dpv_loc_owl:VU
class_uri: loc:VU

```
</details>

### Induced

<details>
```yaml
name: VU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Vanuatu
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Vanuatu
exact_mappings:
- dpv_loc:VU
- dpv_loc_owl:VU
class_uri: loc:VU

```
</details></div>