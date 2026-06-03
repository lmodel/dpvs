---
search:
  boost: 10.0
---

# Class: FRPDL 


_Concept representing region Pays de la Loire in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-PDL](https://w3id.org/lmodel/dpv/loc/FR-PDL)





```mermaid
 classDiagram
    class FRPDL
    click FRPDL href "../FRPDL/"
      FR <|-- FRPDL
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRPDL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-PDL](https://w3id.org/lmodel/dpv/loc/FR-PDL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-PDL
* Pays de la Loire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-PDL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-PDL |
| native | loc:FRPDL |
| exact | dpv_loc:FR-PDL, dpv_loc_owl:FR-PDL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRPDL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-PDL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Pays de la Loire in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-PDL
- Pays de la Loire
exact_mappings:
- dpv_loc:FR-PDL
- dpv_loc_owl:FR-PDL
is_a: FR
class_uri: loc:FR-PDL

```
</details>

### Induced

<details>
```yaml
name: FRPDL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-PDL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Pays de la Loire in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-PDL
- Pays de la Loire
exact_mappings:
- dpv_loc:FR-PDL
- dpv_loc_owl:FR-PDL
is_a: FR
class_uri: loc:FR-PDL

```
</details></div>