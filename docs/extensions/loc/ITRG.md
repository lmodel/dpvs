---
search:
  boost: 10.0
---

# Class: ITRG 


_Concept representing region Province of Ragusa in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-RG](https://w3id.org/lmodel/dpv/loc/IT-RG)





```mermaid
 classDiagram
    class ITRG
    click ITRG href "../ITRG/"
      IT <|-- ITRG
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITRG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-RG](https://w3id.org/lmodel/dpv/loc/IT-RG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-RG
* Province of Ragusa




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-RG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-RG |
| native | loc:ITRG |
| exact | dpv_loc:IT-RG, dpv_loc_owl:IT-RG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITRG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-RG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ragusa in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-RG
- Province of Ragusa
exact_mappings:
- dpv_loc:IT-RG
- dpv_loc_owl:IT-RG
is_a: IT
class_uri: loc:IT-RG

```
</details>

### Induced

<details>
```yaml
name: ITRG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-RG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ragusa in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-RG
- Province of Ragusa
exact_mappings:
- dpv_loc:IT-RG
- dpv_loc_owl:IT-RG
is_a: IT
class_uri: loc:IT-RG

```
</details></div>