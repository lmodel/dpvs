---
search:
  boost: 10.0
---

# Class: FROCC 


_Concept representing region Occitanie in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-OCC](https://w3id.org/lmodel/dpv/loc/FR-OCC)





```mermaid
 classDiagram
    class FROCC
    click FROCC href "../FROCC/"
      FR <|-- FROCC
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FROCC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-OCC](https://w3id.org/lmodel/dpv/loc/FR-OCC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-OCC
* Occitanie




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-OCC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-OCC |
| native | loc:FROCC |
| exact | dpv_loc:FR-OCC, dpv_loc_owl:FR-OCC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FROCC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-OCC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Occitanie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-OCC
- Occitanie
exact_mappings:
- dpv_loc:FR-OCC
- dpv_loc_owl:FR-OCC
is_a: FR
class_uri: loc:FR-OCC

```
</details>

### Induced

<details>
```yaml
name: FROCC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-OCC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Occitanie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-OCC
- Occitanie
exact_mappings:
- dpv_loc:FR-OCC
- dpv_loc_owl:FR-OCC
is_a: FR
class_uri: loc:FR-OCC

```
</details></div>