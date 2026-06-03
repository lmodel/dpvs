---
search:
  boost: 10.0
---

# Class: FRGES 


_Concept representing region Grand Est in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-GES](https://w3id.org/lmodel/dpv/loc/FR-GES)





```mermaid
 classDiagram
    class FRGES
    click FRGES href "../FRGES/"
      FR <|-- FRGES
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRGES**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-GES](https://w3id.org/lmodel/dpv/loc/FR-GES) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-GES
* Grand Est




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-GES |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-GES |
| native | loc:FRGES |
| exact | dpv_loc:FR-GES, dpv_loc_owl:FR-GES |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRGES
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-GES
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Grand Est in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-GES
- Grand Est
exact_mappings:
- dpv_loc:FR-GES
- dpv_loc_owl:FR-GES
is_a: FR
class_uri: loc:FR-GES

```
</details>

### Induced

<details>
```yaml
name: FRGES
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-GES
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Grand Est in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-GES
- Grand Est
exact_mappings:
- dpv_loc:FR-GES
- dpv_loc_owl:FR-GES
is_a: FR
class_uri: loc:FR-GES

```
</details></div>