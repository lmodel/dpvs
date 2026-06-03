---
search:
  boost: 10.0
---

# Class: ISFLR 


_Concept representing region Fljótsdalshreppur in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-FLR](https://w3id.org/lmodel/dpv/loc/IS-FLR)





```mermaid
 classDiagram
    class ISFLR
    click ISFLR href "../ISFLR/"
      IS <|-- ISFLR
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISFLR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-FLR](https://w3id.org/lmodel/dpv/loc/IS-FLR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-FLR
* Fljótsdalshreppur




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-FLR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-FLR |
| native | loc:ISFLR |
| exact | dpv_loc:IS-FLR, dpv_loc_owl:IS-FLR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISFLR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-FLR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Fljótsdalshreppur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-FLR
- Fljótsdalshreppur
exact_mappings:
- dpv_loc:IS-FLR
- dpv_loc_owl:IS-FLR
is_a: IS
class_uri: loc:IS-FLR

```
</details>

### Induced

<details>
```yaml
name: ISFLR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-FLR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Fljótsdalshreppur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-FLR
- Fljótsdalshreppur
exact_mappings:
- dpv_loc:IS-FLR
- dpv_loc_owl:IS-FLR
is_a: IS
class_uri: loc:IS-FLR

```
</details></div>