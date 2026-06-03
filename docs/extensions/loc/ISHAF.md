---
search:
  boost: 10.0
---

# Class: ISHAF 


_Concept representing region Hafnarfjörður in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-HAF](https://w3id.org/lmodel/dpv/loc/IS-HAF)





```mermaid
 classDiagram
    class ISHAF
    click ISHAF href "../ISHAF/"
      IS <|-- ISHAF
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISHAF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-HAF](https://w3id.org/lmodel/dpv/loc/IS-HAF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-HAF
* Hafnarfjörður




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-HAF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-HAF |
| native | loc:ISHAF |
| exact | dpv_loc:IS-HAF, dpv_loc_owl:IS-HAF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISHAF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-HAF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hafnarfjörður in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-HAF
- Hafnarfjörður
exact_mappings:
- dpv_loc:IS-HAF
- dpv_loc_owl:IS-HAF
is_a: IS
class_uri: loc:IS-HAF

```
</details>

### Induced

<details>
```yaml
name: ISHAF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-HAF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hafnarfjörður in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-HAF
- Hafnarfjörður
exact_mappings:
- dpv_loc:IS-HAF
- dpv_loc_owl:IS-HAF
is_a: IS
class_uri: loc:IS-HAF

```
</details></div>