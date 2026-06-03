---
search:
  boost: 10.0
---

# Class: FRHDF 


_Concept representing region Hauts-de-France in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-HDF](https://w3id.org/lmodel/dpv/loc/FR-HDF)





```mermaid
 classDiagram
    class FRHDF
    click FRHDF href "../FRHDF/"
      FR <|-- FRHDF
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRHDF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-HDF](https://w3id.org/lmodel/dpv/loc/FR-HDF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-HDF
* Hauts-de-France




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-HDF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-HDF |
| native | loc:FRHDF |
| exact | dpv_loc:FR-HDF, dpv_loc_owl:FR-HDF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRHDF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-HDF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hauts-de-France in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-HDF
- Hauts-de-France
exact_mappings:
- dpv_loc:FR-HDF
- dpv_loc_owl:FR-HDF
is_a: FR
class_uri: loc:FR-HDF

```
</details>

### Induced

<details>
```yaml
name: FRHDF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-HDF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hauts-de-France in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-HDF
- Hauts-de-France
exact_mappings:
- dpv_loc:FR-HDF
- dpv_loc_owl:FR-HDF
is_a: FR
class_uri: loc:FR-HDF

```
</details></div>