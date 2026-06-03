---
search:
  boost: 10.0
---

# Class: ITPI 


_Concept representing region Province of Pisa in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PI](https://w3id.org/lmodel/dpv/loc/IT-PI)





```mermaid
 classDiagram
    class ITPI
    click ITPI href "../ITPI/"
      IT <|-- ITPI
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PI](https://w3id.org/lmodel/dpv/loc/IT-PI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PI
* Province of Pisa




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PI |
| native | loc:ITPI |
| exact | dpv_loc:IT-PI, dpv_loc_owl:IT-PI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pisa in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PI
- Province of Pisa
exact_mappings:
- dpv_loc:IT-PI
- dpv_loc_owl:IT-PI
is_a: IT
class_uri: loc:IT-PI

```
</details>

### Induced

<details>
```yaml
name: ITPI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pisa in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PI
- Province of Pisa
exact_mappings:
- dpv_loc:IT-PI
- dpv_loc_owl:IT-PI
is_a: IT
class_uri: loc:IT-PI

```
</details></div>