---
search:
  boost: 10.0
---

# Class: ROTR 


_Concept representing region Teleorman County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-TR](https://w3id.org/lmodel/dpv/loc/RO-TR)





```mermaid
 classDiagram
    class ROTR
    click ROTR href "../ROTR/"
      RO <|-- ROTR
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROTR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-TR](https://w3id.org/lmodel/dpv/loc/RO-TR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-TR
* Teleorman County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-TR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-TR |
| native | loc:ROTR |
| exact | dpv_loc:RO-TR, dpv_loc_owl:RO-TR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROTR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-TR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Teleorman County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-TR
- Teleorman County
exact_mappings:
- dpv_loc:RO-TR
- dpv_loc_owl:RO-TR
is_a: RO
class_uri: loc:RO-TR

```
</details>

### Induced

<details>
```yaml
name: ROTR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-TR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Teleorman County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-TR
- Teleorman County
exact_mappings:
- dpv_loc:RO-TR
- dpv_loc_owl:RO-TR
is_a: RO
class_uri: loc:RO-TR

```
</details></div>