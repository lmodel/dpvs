---
search:
  boost: 10.0
---

# Class: ITIM 


_Concept representing region Province of Imperia in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-IM](https://w3id.org/lmodel/dpv/loc/IT-IM)





```mermaid
 classDiagram
    class ITIM
    click ITIM href "../ITIM/"
      IT <|-- ITIM
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITIM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-IM](https://w3id.org/lmodel/dpv/loc/IT-IM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-IM
* Province of Imperia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-IM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-IM |
| native | loc:ITIM |
| exact | dpv_loc:IT-IM, dpv_loc_owl:IT-IM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITIM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-IM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Imperia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-IM
- Province of Imperia
exact_mappings:
- dpv_loc:IT-IM
- dpv_loc_owl:IT-IM
is_a: IT
class_uri: loc:IT-IM

```
</details>

### Induced

<details>
```yaml
name: ITIM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-IM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Imperia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-IM
- Province of Imperia
exact_mappings:
- dpv_loc:IT-IM
- dpv_loc_owl:IT-IM
is_a: IT
class_uri: loc:IT-IM

```
</details></div>