---
search:
  boost: 10.0
---

# Class: ISSTR 


_Concept representing region Strandabyggð in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-STR](https://w3id.org/lmodel/dpv/loc/IS-STR)





```mermaid
 classDiagram
    class ISSTR
    click ISSTR href "../ISSTR/"
      IS <|-- ISSTR
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISSTR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-STR](https://w3id.org/lmodel/dpv/loc/IS-STR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-STR
* Strandabyggð




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-STR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-STR |
| native | loc:ISSTR |
| exact | dpv_loc:IS-STR, dpv_loc_owl:IS-STR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISSTR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-STR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Strandabyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-STR
- Strandabyggð
exact_mappings:
- dpv_loc:IS-STR
- dpv_loc_owl:IS-STR
is_a: IS
class_uri: loc:IS-STR

```
</details>

### Induced

<details>
```yaml
name: ISSTR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-STR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Strandabyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-STR
- Strandabyggð
exact_mappings:
- dpv_loc:IS-STR
- dpv_loc_owl:IS-STR
is_a: IS
class_uri: loc:IS-STR

```
</details></div>