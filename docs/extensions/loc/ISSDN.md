---
search:
  boost: 10.0
---

# Class: ISSDN 


_Concept representing region Suðurnesjabær in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-SDN](https://w3id.org/lmodel/dpv/loc/IS-SDN)





```mermaid
 classDiagram
    class ISSDN
    click ISSDN href "../ISSDN/"
      IS <|-- ISSDN
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISSDN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-SDN](https://w3id.org/lmodel/dpv/loc/IS-SDN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-SDN
* Suðurnesjabær




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-SDN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-SDN |
| native | loc:ISSDN |
| exact | dpv_loc:IS-SDN, dpv_loc_owl:IS-SDN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISSDN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-SDN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Suðurnesjabær in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-SDN
- Suðurnesjabær
exact_mappings:
- dpv_loc:IS-SDN
- dpv_loc_owl:IS-SDN
is_a: IS
class_uri: loc:IS-SDN

```
</details>

### Induced

<details>
```yaml
name: ISSDN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-SDN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Suðurnesjabær in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-SDN
- Suðurnesjabær
exact_mappings:
- dpv_loc:IS-SDN
- dpv_loc_owl:IS-SDN
is_a: IS
class_uri: loc:IS-SDN

```
</details></div>