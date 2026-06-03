---
search:
  boost: 10.0
---

# Class: ITFE 


_Concept representing region Province of Ferrara in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-FE](https://w3id.org/lmodel/dpv/loc/IT-FE)





```mermaid
 classDiagram
    class ITFE
    click ITFE href "../ITFE/"
      IT <|-- ITFE
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITFE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-FE](https://w3id.org/lmodel/dpv/loc/IT-FE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-FE
* Province of Ferrara




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-FE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-FE |
| native | loc:ITFE |
| exact | dpv_loc:IT-FE, dpv_loc_owl:IT-FE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITFE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-FE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ferrara in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-FE
- Province of Ferrara
exact_mappings:
- dpv_loc:IT-FE
- dpv_loc_owl:IT-FE
is_a: IT
class_uri: loc:IT-FE

```
</details>

### Induced

<details>
```yaml
name: ITFE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-FE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ferrara in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-FE
- Province of Ferrara
exact_mappings:
- dpv_loc:IT-FE
- dpv_loc_owl:IT-FE
is_a: IT
class_uri: loc:IT-FE

```
</details></div>