---
search:
  boost: 10.0
---

# Class: IS0 


_Concept representing region Reykjavík in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-0](https://w3id.org/lmodel/dpv/loc/IS-0)





```mermaid
 classDiagram
    class IS0
    click IS0 href "../IS0/"
      IS <|-- IS0
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **IS0**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-0](https://w3id.org/lmodel/dpv/loc/IS-0) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-0
* Reykjavík




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-0 |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-0 |
| native | loc:IS0 |
| exact | dpv_loc:IS-0, dpv_loc_owl:IS-0 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IS0
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-0
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Reykjavík in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-0
- Reykjavík
exact_mappings:
- dpv_loc:IS-0
- dpv_loc_owl:IS-0
is_a: IS
class_uri: loc:IS-0

```
</details>

### Induced

<details>
```yaml
name: IS0
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-0
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Reykjavík in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-0
- Reykjavík
exact_mappings:
- dpv_loc:IS-0
- dpv_loc_owl:IS-0
is_a: IS
class_uri: loc:IS-0

```
</details></div>