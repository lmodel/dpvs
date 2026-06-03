---
search:
  boost: 10.0
---

# Class: FRNC 


_Concept representing region New Caledonia in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-NC](https://w3id.org/lmodel/dpv/loc/FR-NC)





```mermaid
 classDiagram
    class FRNC
    click FRNC href "../FRNC/"
      FR <|-- FRNC
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRNC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-NC](https://w3id.org/lmodel/dpv/loc/FR-NC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-NC
* New Caledonia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-NC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-NC |
| native | loc:FRNC |
| exact | dpv_loc:FR-NC, dpv_loc_owl:FR-NC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRNC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-NC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region New Caledonia in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-NC
- New Caledonia
exact_mappings:
- dpv_loc:FR-NC
- dpv_loc_owl:FR-NC
is_a: FR
class_uri: loc:FR-NC

```
</details>

### Induced

<details>
```yaml
name: FRNC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-NC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region New Caledonia in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-NC
- New Caledonia
exact_mappings:
- dpv_loc:FR-NC
- dpv_loc_owl:FR-NC
is_a: FR
class_uri: loc:FR-NC

```
</details></div>