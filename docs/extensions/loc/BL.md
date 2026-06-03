---
search:
  boost: 10.0
---

# Class: BL 


_Concept representing Country of Saint Barthélemy_



<div data-search-exclude markdown="1">



URI: [loc:BL](https://w3id.org/lmodel/dpv/loc/BL)





```mermaid
 classDiagram
    class BL
    click BL href "../BL/"
      FR <|-- BL
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **BL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BL](https://w3id.org/lmodel/dpv/loc/BL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Saint Barthélemy




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BL |
| native | loc:BL |
| exact | dpv_loc:BL, dpv_loc_owl:BL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Saint Barthélemy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Saint Barthélemy
exact_mappings:
- dpv_loc:BL
- dpv_loc_owl:BL
is_a: FR
class_uri: loc:BL

```
</details>

### Induced

<details>
```yaml
name: BL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Saint Barthélemy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Saint Barthélemy
exact_mappings:
- dpv_loc:BL
- dpv_loc_owl:BL
is_a: FR
class_uri: loc:BL

```
</details></div>