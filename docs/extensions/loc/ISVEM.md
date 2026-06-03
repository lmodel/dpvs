---
search:
  boost: 10.0
---

# Class: ISVEM 


_Concept representing region Vestmannaeyjar in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-VEM](https://w3id.org/lmodel/dpv/loc/IS-VEM)





```mermaid
 classDiagram
    class ISVEM
    click ISVEM href "../ISVEM/"
      IS <|-- ISVEM
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISVEM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-VEM](https://w3id.org/lmodel/dpv/loc/IS-VEM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-VEM
* Vestmannaeyjar




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-VEM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-VEM |
| native | loc:ISVEM |
| exact | dpv_loc:IS-VEM, dpv_loc_owl:IS-VEM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISVEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-VEM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vestmannaeyjar in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-VEM
- Vestmannaeyjar
exact_mappings:
- dpv_loc:IS-VEM
- dpv_loc_owl:IS-VEM
is_a: IS
class_uri: loc:IS-VEM

```
</details>

### Induced

<details>
```yaml
name: ISVEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-VEM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vestmannaeyjar in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-VEM
- Vestmannaeyjar
exact_mappings:
- dpv_loc:IS-VEM
- dpv_loc_owl:IS-VEM
is_a: IS
class_uri: loc:IS-VEM

```
</details></div>