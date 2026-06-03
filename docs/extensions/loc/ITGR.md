---
search:
  boost: 10.0
---

# Class: ITGR 


_Concept representing region Province of Grosseto in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-GR](https://w3id.org/lmodel/dpv/loc/IT-GR)





```mermaid
 classDiagram
    class ITGR
    click ITGR href "../ITGR/"
      IT <|-- ITGR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITGR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-GR](https://w3id.org/lmodel/dpv/loc/IT-GR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-GR
* Province of Grosseto




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-GR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-GR |
| native | loc:ITGR |
| exact | dpv_loc:IT-GR, dpv_loc_owl:IT-GR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITGR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-GR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Grosseto in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-GR
- Province of Grosseto
exact_mappings:
- dpv_loc:IT-GR
- dpv_loc_owl:IT-GR
is_a: IT
class_uri: loc:IT-GR

```
</details>

### Induced

<details>
```yaml
name: ITGR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-GR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Grosseto in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-GR
- Province of Grosseto
exact_mappings:
- dpv_loc:IT-GR
- dpv_loc_owl:IT-GR
is_a: IT
class_uri: loc:IT-GR

```
</details></div>