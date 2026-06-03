---
search:
  boost: 10.0
---

# Class: ISBOG 


_Concept representing region Borgarbyggð in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-BOG](https://w3id.org/lmodel/dpv/loc/IS-BOG)





```mermaid
 classDiagram
    class ISBOG
    click ISBOG href "../ISBOG/"
      IS <|-- ISBOG
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISBOG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-BOG](https://w3id.org/lmodel/dpv/loc/IS-BOG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-BOG
* Borgarbyggð




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-BOG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-BOG |
| native | loc:ISBOG |
| exact | dpv_loc:IS-BOG, dpv_loc_owl:IS-BOG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISBOG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-BOG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Borgarbyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-BOG
- Borgarbyggð
exact_mappings:
- dpv_loc:IS-BOG
- dpv_loc_owl:IS-BOG
is_a: IS
class_uri: loc:IS-BOG

```
</details>

### Induced

<details>
```yaml
name: ISBOG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-BOG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Borgarbyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-BOG
- Borgarbyggð
exact_mappings:
- dpv_loc:IS-BOG
- dpv_loc_owl:IS-BOG
is_a: IS
class_uri: loc:IS-BOG

```
</details></div>