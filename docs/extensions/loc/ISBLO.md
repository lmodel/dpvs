---
search:
  boost: 10.0
---

# Class: ISBLO 


_Concept representing region Blönduós in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-BLO](https://w3id.org/lmodel/dpv/loc/IS-BLO)





```mermaid
 classDiagram
    class ISBLO
    click ISBLO href "../ISBLO/"
      IS <|-- ISBLO
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISBLO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-BLO](https://w3id.org/lmodel/dpv/loc/IS-BLO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-BLO
* Blönduós




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-BLO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-BLO |
| native | loc:ISBLO |
| exact | dpv_loc:IS-BLO, dpv_loc_owl:IS-BLO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISBLO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-BLO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Blönduós in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-BLO
- Blönduós
exact_mappings:
- dpv_loc:IS-BLO
- dpv_loc_owl:IS-BLO
is_a: IS
class_uri: loc:IS-BLO

```
</details>

### Induced

<details>
```yaml
name: ISBLO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-BLO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Blönduós in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-BLO
- Blönduós
exact_mappings:
- dpv_loc:IS-BLO
- dpv_loc_owl:IS-BLO
is_a: IS
class_uri: loc:IS-BLO

```
</details></div>