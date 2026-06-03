---
search:
  boost: 10.0
---

# Class: ITLC 


_Concept representing region Province of Lecco in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-LC](https://w3id.org/lmodel/dpv/loc/IT-LC)





```mermaid
 classDiagram
    class ITLC
    click ITLC href "../ITLC/"
      IT <|-- ITLC
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITLC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-LC](https://w3id.org/lmodel/dpv/loc/IT-LC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-LC
* Province of Lecco




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-LC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-LC |
| native | loc:ITLC |
| exact | dpv_loc:IT-LC, dpv_loc_owl:IT-LC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITLC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-LC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lecco in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-LC
- Province of Lecco
exact_mappings:
- dpv_loc:IT-LC
- dpv_loc_owl:IT-LC
is_a: IT
class_uri: loc:IT-LC

```
</details>

### Induced

<details>
```yaml
name: ITLC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-LC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lecco in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-LC
- Province of Lecco
exact_mappings:
- dpv_loc:IT-LC
- dpv_loc_owl:IT-LC
is_a: IT
class_uri: loc:IT-LC

```
</details></div>