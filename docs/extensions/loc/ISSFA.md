---
search:
  boost: 10.0
---

# Class: ISSFA 


_Concept representing region Árborg in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-SFA](https://w3id.org/lmodel/dpv/loc/IS-SFA)





```mermaid
 classDiagram
    class ISSFA
    click ISSFA href "../ISSFA/"
      IS <|-- ISSFA
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISSFA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-SFA](https://w3id.org/lmodel/dpv/loc/IS-SFA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-SFA
* Árborg




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-SFA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-SFA |
| native | loc:ISSFA |
| exact | dpv_loc:IS-SFA, dpv_loc_owl:IS-SFA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISSFA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-SFA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Árborg in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-SFA
- Árborg
exact_mappings:
- dpv_loc:IS-SFA
- dpv_loc_owl:IS-SFA
is_a: IS
class_uri: loc:IS-SFA

```
</details>

### Induced

<details>
```yaml
name: ISSFA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-SFA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Árborg in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-SFA
- Árborg
exact_mappings:
- dpv_loc:IS-SFA
- dpv_loc_owl:IS-SFA
is_a: IS
class_uri: loc:IS-SFA

```
</details></div>