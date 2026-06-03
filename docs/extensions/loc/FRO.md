---
search:
  boost: 10.0
---

# Class: FRO 


_Concept representing region Nord-Pas-de-Calais in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-O](https://w3id.org/lmodel/dpv/loc/FR-O)





```mermaid
 classDiagram
    class FRO
    click FRO href "../FRO/"
      FR <|-- FRO
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-O](https://w3id.org/lmodel/dpv/loc/FR-O) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-O
* Nord-Pas-de-Calais




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-O |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-O |
| native | loc:FRO |
| exact | dpv_loc:FR-O, dpv_loc_owl:FR-O |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-O
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nord-Pas-de-Calais in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-O
- Nord-Pas-de-Calais
exact_mappings:
- dpv_loc:FR-O
- dpv_loc_owl:FR-O
is_a: FR
class_uri: loc:FR-O

```
</details>

### Induced

<details>
```yaml
name: FRO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-O
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nord-Pas-de-Calais in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-O
- Nord-Pas-de-Calais
exact_mappings:
- dpv_loc:FR-O
- dpv_loc_owl:FR-O
is_a: FR
class_uri: loc:FR-O

```
</details></div>