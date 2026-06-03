---
search:
  boost: 10.0
---

# Class: ITPT 


_Concept representing region Province of Pistoia in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PT](https://w3id.org/lmodel/dpv/loc/IT-PT)





```mermaid
 classDiagram
    class ITPT
    click ITPT href "../ITPT/"
      IT <|-- ITPT
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PT](https://w3id.org/lmodel/dpv/loc/IT-PT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PT
* Province of Pistoia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PT |
| native | loc:ITPT |
| exact | dpv_loc:IT-PT, dpv_loc_owl:IT-PT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pistoia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PT
- Province of Pistoia
exact_mappings:
- dpv_loc:IT-PT
- dpv_loc_owl:IT-PT
is_a: IT
class_uri: loc:IT-PT

```
</details>

### Induced

<details>
```yaml
name: ITPT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pistoia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PT
- Province of Pistoia
exact_mappings:
- dpv_loc:IT-PT
- dpv_loc_owl:IT-PT
is_a: IT
class_uri: loc:IT-PT

```
</details></div>