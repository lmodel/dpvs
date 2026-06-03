---
search:
  boost: 10.0
---

# Class: VNHN 


_Concept representing region Hanoi in country Viet Nam_



<div data-search-exclude markdown="1">



URI: [loc:VN-HN](https://w3id.org/lmodel/dpv/loc/VN-HN)





```mermaid
 classDiagram
    class VNHN
    click VNHN href "../VNHN/"
      VN <|-- VNHN
        click VN href "../VN/"
      
      
```





## Inheritance
* [VN](VN.md)
    * **VNHN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:VN-HN](https://w3id.org/lmodel/dpv/loc/VN-HN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* VN-HN
* Hanoi




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#VN-HN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:VN-HN |
| native | loc:VNHN |
| exact | dpv_loc:VN-HN, dpv_loc_owl:VN-HN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VNHN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VN-HN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hanoi in country Viet Nam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VN-HN
- Hanoi
exact_mappings:
- dpv_loc:VN-HN
- dpv_loc_owl:VN-HN
is_a: VN
class_uri: loc:VN-HN

```
</details>

### Induced

<details>
```yaml
name: VNHN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VN-HN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hanoi in country Viet Nam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VN-HN
- Hanoi
exact_mappings:
- dpv_loc:VN-HN
- dpv_loc_owl:VN-HN
is_a: VN
class_uri: loc:VN-HN

```
</details></div>