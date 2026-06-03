---
search:
  boost: 10.0
---

# Class: ISRKV 


_Concept representing region Reykjavík in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-RKV](https://w3id.org/lmodel/dpv/loc/IS-RKV)





```mermaid
 classDiagram
    class ISRKV
    click ISRKV href "../ISRKV/"
      IS <|-- ISRKV
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISRKV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-RKV](https://w3id.org/lmodel/dpv/loc/IS-RKV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-RKV
* Reykjavík




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-RKV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-RKV |
| native | loc:ISRKV |
| exact | dpv_loc:IS-RKV, dpv_loc_owl:IS-RKV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISRKV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-RKV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Reykjavík in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-RKV
- Reykjavík
exact_mappings:
- dpv_loc:IS-RKV
- dpv_loc_owl:IS-RKV
is_a: IS
class_uri: loc:IS-RKV

```
</details>

### Induced

<details>
```yaml
name: ISRKV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-RKV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Reykjavík in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-RKV
- Reykjavík
exact_mappings:
- dpv_loc:IS-RKV
- dpv_loc_owl:IS-RKV
is_a: IS
class_uri: loc:IS-RKV

```
</details></div>