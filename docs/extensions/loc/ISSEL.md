---
search:
  boost: 10.0
---

# Class: ISSEL 


_Concept representing region Seltjarnarnes in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-SEL](https://w3id.org/lmodel/dpv/loc/IS-SEL)





```mermaid
 classDiagram
    class ISSEL
    click ISSEL href "../ISSEL/"
      IS <|-- ISSEL
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISSEL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-SEL](https://w3id.org/lmodel/dpv/loc/IS-SEL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-SEL
* Seltjarnarnes




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-SEL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-SEL |
| native | loc:ISSEL |
| exact | dpv_loc:IS-SEL, dpv_loc_owl:IS-SEL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISSEL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-SEL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Seltjarnarnes in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-SEL
- Seltjarnarnes
exact_mappings:
- dpv_loc:IS-SEL
- dpv_loc_owl:IS-SEL
is_a: IS
class_uri: loc:IS-SEL

```
</details>

### Induced

<details>
```yaml
name: ISSEL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-SEL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Seltjarnarnes in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-SEL
- Seltjarnarnes
exact_mappings:
- dpv_loc:IS-SEL
- dpv_loc_owl:IS-SEL
is_a: IS
class_uri: loc:IS-SEL

```
</details></div>