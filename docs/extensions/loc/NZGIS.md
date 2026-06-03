---
search:
  boost: 10.0
---

# Class: NZGIS 


_Concept representing region Gisborne District in country New Zealand_



<div data-search-exclude markdown="1">



URI: [loc:NZ-GIS](https://w3id.org/lmodel/dpv/loc/NZ-GIS)





```mermaid
 classDiagram
    class NZGIS
    click NZGIS href "../NZGIS/"
      NZ <|-- NZGIS
        click NZ href "../NZ/"
      
      
```





## Inheritance
* [NZ](NZ.md)
    * **NZGIS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NZ-GIS](https://w3id.org/lmodel/dpv/loc/NZ-GIS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NZ-GIS
* Gisborne District




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NZ-GIS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NZ-GIS |
| native | loc:NZGIS |
| exact | dpv_loc:NZ-GIS, dpv_loc_owl:NZ-GIS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NZGIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-GIS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gisborne District in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-GIS
- Gisborne District
exact_mappings:
- dpv_loc:NZ-GIS
- dpv_loc_owl:NZ-GIS
is_a: NZ
class_uri: loc:NZ-GIS

```
</details>

### Induced

<details>
```yaml
name: NZGIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-GIS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gisborne District in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-GIS
- Gisborne District
exact_mappings:
- dpv_loc:NZ-GIS
- dpv_loc_owl:NZ-GIS
is_a: NZ
class_uri: loc:NZ-GIS

```
</details></div>