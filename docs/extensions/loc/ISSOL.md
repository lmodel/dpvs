---
search:
  boost: 10.0
---

# Class: ISSOL 


_Concept representing region Sveitarfélagið Ölfus in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-SOL](https://w3id.org/lmodel/dpv/loc/IS-SOL)





```mermaid
 classDiagram
    class ISSOL
    click ISSOL href "../ISSOL/"
      IS <|-- ISSOL
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISSOL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-SOL](https://w3id.org/lmodel/dpv/loc/IS-SOL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-SOL
* Sveitarfélagið Ölfus




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-SOL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-SOL |
| native | loc:ISSOL |
| exact | dpv_loc:IS-SOL, dpv_loc_owl:IS-SOL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISSOL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-SOL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Sveitarfélagið Ölfus in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-SOL
- Sveitarfélagið Ölfus
exact_mappings:
- dpv_loc:IS-SOL
- dpv_loc_owl:IS-SOL
is_a: IS
class_uri: loc:IS-SOL

```
</details>

### Induced

<details>
```yaml
name: ISSOL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-SOL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Sveitarfélagið Ölfus in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-SOL
- Sveitarfélagið Ölfus
exact_mappings:
- dpv_loc:IS-SOL
- dpv_loc_owl:IS-SOL
is_a: IS
class_uri: loc:IS-SOL

```
</details></div>