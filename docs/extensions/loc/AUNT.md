---
search:
  boost: 10.0
---

# Class: AUNT 


_Concept representing region Northern Territory in country Australia_



<div data-search-exclude markdown="1">



URI: [loc:AU-NT](https://w3id.org/lmodel/dpv/loc/AU-NT)





```mermaid
 classDiagram
    class AUNT
    click AUNT href "../AUNT/"
      AU <|-- AUNT
        click AU href "../AU/"
      
      
```





## Inheritance
* [AU](AU.md)
    * **AUNT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AU-NT](https://w3id.org/lmodel/dpv/loc/AU-NT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* AU-NT
* Northern Territory




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AU-NT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AU-NT |
| native | loc:AUNT |
| exact | dpv_loc:AU-NT, dpv_loc_owl:AU-NT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AUNT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AU-NT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Northern Territory in country Australia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AU-NT
- Northern Territory
exact_mappings:
- dpv_loc:AU-NT
- dpv_loc_owl:AU-NT
is_a: AU
class_uri: loc:AU-NT

```
</details>

### Induced

<details>
```yaml
name: AUNT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AU-NT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Northern Territory in country Australia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AU-NT
- Northern Territory
exact_mappings:
- dpv_loc:AU-NT
- dpv_loc_owl:AU-NT
is_a: AU
class_uri: loc:AU-NT

```
</details></div>