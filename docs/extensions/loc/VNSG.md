---
search:
  boost: 10.0
---

# Class: VNSG 


_Concept representing region Ho Chi Minh City in country Viet Nam_



<div data-search-exclude markdown="1">



URI: [loc:VN-SG](https://w3id.org/lmodel/dpv/loc/VN-SG)





```mermaid
 classDiagram
    class VNSG
    click VNSG href "../VNSG/"
      VN <|-- VNSG
        click VN href "../VN/"
      
      
```





## Inheritance
* [VN](VN.md)
    * **VNSG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:VN-SG](https://w3id.org/lmodel/dpv/loc/VN-SG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* VN-SG
* Ho Chi Minh City




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#VN-SG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:VN-SG |
| native | loc:VNSG |
| exact | dpv_loc:VN-SG, dpv_loc_owl:VN-SG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VNSG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VN-SG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ho Chi Minh City in country Viet Nam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VN-SG
- Ho Chi Minh City
exact_mappings:
- dpv_loc:VN-SG
- dpv_loc_owl:VN-SG
is_a: VN
class_uri: loc:VN-SG

```
</details>

### Induced

<details>
```yaml
name: VNSG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VN-SG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ho Chi Minh City in country Viet Nam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VN-SG
- Ho Chi Minh City
exact_mappings:
- dpv_loc:VN-SG
- dpv_loc_owl:VN-SG
is_a: VN
class_uri: loc:VN-SG

```
</details></div>