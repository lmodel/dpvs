---
search:
  boost: 10.0
---

# Class: SKKI 


_Concept representing region Košice Region in country Slovakia_



<div data-search-exclude markdown="1">



URI: [loc:SK-KI](https://w3id.org/lmodel/dpv/loc/SK-KI)





```mermaid
 classDiagram
    class SKKI
    click SKKI href "../SKKI/"
      SK <|-- SKKI
        click SK href "../SK/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SK](SK.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SKKI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SK-KI](https://w3id.org/lmodel/dpv/loc/SK-KI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SK-KI
* Košice Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SK-KI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SK-KI |
| native | loc:SKKI |
| exact | dpv_loc:SK-KI, dpv_loc_owl:SK-KI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SKKI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-KI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Košice Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-KI
- Košice Region
exact_mappings:
- dpv_loc:SK-KI
- dpv_loc_owl:SK-KI
is_a: SK
class_uri: loc:SK-KI

```
</details>

### Induced

<details>
```yaml
name: SKKI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-KI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Košice Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-KI
- Košice Region
exact_mappings:
- dpv_loc:SK-KI
- dpv_loc_owl:SK-KI
is_a: SK
class_uri: loc:SK-KI

```
</details></div>