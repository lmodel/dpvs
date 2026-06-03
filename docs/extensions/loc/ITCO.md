---
search:
  boost: 10.0
---

# Class: ITCO 


_Concept representing region Province of Como in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-CO](https://w3id.org/lmodel/dpv/loc/IT-CO)





```mermaid
 classDiagram
    class ITCO
    click ITCO href "../ITCO/"
      IT <|-- ITCO
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITCO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-CO](https://w3id.org/lmodel/dpv/loc/IT-CO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-CO
* Province of Como




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-CO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-CO |
| native | loc:ITCO |
| exact | dpv_loc:IT-CO, dpv_loc_owl:IT-CO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITCO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Como in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CO
- Province of Como
exact_mappings:
- dpv_loc:IT-CO
- dpv_loc_owl:IT-CO
is_a: IT
class_uri: loc:IT-CO

```
</details>

### Induced

<details>
```yaml
name: ITCO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Como in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CO
- Province of Como
exact_mappings:
- dpv_loc:IT-CO
- dpv_loc_owl:IT-CO
is_a: IT
class_uri: loc:IT-CO

```
</details></div>