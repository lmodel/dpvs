---
search:
  boost: 10.0
---

# Class: ITFG 


_Concept representing region Province of Foggia in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-FG](https://w3id.org/lmodel/dpv/loc/IT-FG)





```mermaid
 classDiagram
    class ITFG
    click ITFG href "../ITFG/"
      IT <|-- ITFG
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITFG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-FG](https://w3id.org/lmodel/dpv/loc/IT-FG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-FG
* Province of Foggia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-FG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-FG |
| native | loc:ITFG |
| exact | dpv_loc:IT-FG, dpv_loc_owl:IT-FG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITFG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-FG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Foggia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-FG
- Province of Foggia
exact_mappings:
- dpv_loc:IT-FG
- dpv_loc_owl:IT-FG
is_a: IT
class_uri: loc:IT-FG

```
</details>

### Induced

<details>
```yaml
name: ITFG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-FG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Foggia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-FG
- Province of Foggia
exact_mappings:
- dpv_loc:IT-FG
- dpv_loc_owl:IT-FG
is_a: IT
class_uri: loc:IT-FG

```
</details></div>