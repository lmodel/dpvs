---
search:
  boost: 10.0
---

# Class: PLKI 


_Concept representing region Kielce in country Poland_



<div data-search-exclude markdown="1">



URI: [loc:PL-KI](https://w3id.org/lmodel/dpv/loc/PL-KI)





```mermaid
 classDiagram
    class PLKI
    click PLKI href "../PLKI/"
      PL <|-- PLKI
        click PL href "../PL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [PL](PL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **PLKI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PL-KI](https://w3id.org/lmodel/dpv/loc/PL-KI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* PL-KI
* Kielce




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PL-KI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PL-KI |
| native | loc:PLKI |
| exact | dpv_loc:PL-KI, dpv_loc_owl:PL-KI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PLKI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PL-KI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kielce in country Poland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PL-KI
- Kielce
exact_mappings:
- dpv_loc:PL-KI
- dpv_loc_owl:PL-KI
is_a: PL
class_uri: loc:PL-KI

```
</details>

### Induced

<details>
```yaml
name: PLKI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PL-KI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kielce in country Poland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PL-KI
- Kielce
exact_mappings:
- dpv_loc:PL-KI
- dpv_loc_owl:PL-KI
is_a: PL
class_uri: loc:PL-KI

```
</details></div>