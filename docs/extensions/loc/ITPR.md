---
search:
  boost: 10.0
---

# Class: ITPR 


_Concept representing region Province of Parma in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PR](https://w3id.org/lmodel/dpv/loc/IT-PR)





```mermaid
 classDiagram
    class ITPR
    click ITPR href "../ITPR/"
      IT <|-- ITPR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PR](https://w3id.org/lmodel/dpv/loc/IT-PR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PR
* Province of Parma




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PR |
| native | loc:ITPR |
| exact | dpv_loc:IT-PR, dpv_loc_owl:IT-PR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Parma in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PR
- Province of Parma
exact_mappings:
- dpv_loc:IT-PR
- dpv_loc_owl:IT-PR
is_a: IT
class_uri: loc:IT-PR

```
</details>

### Induced

<details>
```yaml
name: ITPR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Parma in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PR
- Province of Parma
exact_mappings:
- dpv_loc:IT-PR
- dpv_loc_owl:IT-PR
is_a: IT
class_uri: loc:IT-PR

```
</details></div>