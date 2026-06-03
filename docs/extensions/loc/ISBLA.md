---
search:
  boost: 10.0
---

# Class: ISBLA 


_Concept representing region Bláskógabyggð in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-BLA](https://w3id.org/lmodel/dpv/loc/IS-BLA)





```mermaid
 classDiagram
    class ISBLA
    click ISBLA href "../ISBLA/"
      IS <|-- ISBLA
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISBLA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-BLA](https://w3id.org/lmodel/dpv/loc/IS-BLA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-BLA
* Bláskógabyggð




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-BLA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-BLA |
| native | loc:ISBLA |
| exact | dpv_loc:IS-BLA, dpv_loc_owl:IS-BLA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISBLA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-BLA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bláskógabyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-BLA
- Bláskógabyggð
exact_mappings:
- dpv_loc:IS-BLA
- dpv_loc_owl:IS-BLA
is_a: IS
class_uri: loc:IS-BLA

```
</details>

### Induced

<details>
```yaml
name: ISBLA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-BLA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bláskógabyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-BLA
- Bláskógabyggð
exact_mappings:
- dpv_loc:IS-BLA
- dpv_loc_owl:IS-BLA
is_a: IS
class_uri: loc:IS-BLA

```
</details></div>