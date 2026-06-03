---
search:
  boost: 10.0
---

# Class: UYMO 


_Concept representing region Montevideo Department in country Uruguay_



<div data-search-exclude markdown="1">



URI: [loc:UY-MO](https://w3id.org/lmodel/dpv/loc/UY-MO)





```mermaid
 classDiagram
    class UYMO
    click UYMO href "../UYMO/"
      UY <|-- UYMO
        click UY href "../UY/"
      
      
```





## Inheritance
* [UY](UY.md)
    * **UYMO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:UY-MO](https://w3id.org/lmodel/dpv/loc/UY-MO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* UY-MO
* Montevideo Department




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#UY-MO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:UY-MO |
| native | loc:UYMO |
| exact | dpv_loc:UY-MO, dpv_loc_owl:UY-MO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UYMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#UY-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Montevideo Department in country Uruguay
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- UY-MO
- Montevideo Department
exact_mappings:
- dpv_loc:UY-MO
- dpv_loc_owl:UY-MO
is_a: UY
class_uri: loc:UY-MO

```
</details>

### Induced

<details>
```yaml
name: UYMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#UY-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Montevideo Department in country Uruguay
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- UY-MO
- Montevideo Department
exact_mappings:
- dpv_loc:UY-MO
- dpv_loc_owl:UY-MO
is_a: UY
class_uri: loc:UY-MO

```
</details></div>