---
search:
  boost: 10.0
---

# Class: VNHP 


_Concept representing region Haiphong in country Viet Nam_



<div data-search-exclude markdown="1">



URI: [loc:VN-HP](https://w3id.org/lmodel/dpv/loc/VN-HP)





```mermaid
 classDiagram
    class VNHP
    click VNHP href "../VNHP/"
      VN <|-- VNHP
        click VN href "../VN/"
      
      
```





## Inheritance
* [VN](VN.md)
    * **VNHP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:VN-HP](https://w3id.org/lmodel/dpv/loc/VN-HP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* VN-HP
* Haiphong




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#VN-HP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:VN-HP |
| native | loc:VNHP |
| exact | dpv_loc:VN-HP, dpv_loc_owl:VN-HP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VNHP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VN-HP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Haiphong in country Viet Nam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VN-HP
- Haiphong
exact_mappings:
- dpv_loc:VN-HP
- dpv_loc_owl:VN-HP
is_a: VN
class_uri: loc:VN-HP

```
</details>

### Induced

<details>
```yaml
name: VNHP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VN-HP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Haiphong in country Viet Nam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VN-HP
- Haiphong
exact_mappings:
- dpv_loc:VN-HP
- dpv_loc_owl:VN-HP
is_a: VN
class_uri: loc:VN-HP

```
</details></div>