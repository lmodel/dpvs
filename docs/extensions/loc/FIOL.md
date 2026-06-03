---
search:
  boost: 10.0
---

# Class: FIOL 


_Concept representing region Oulu Province in country Finland_



<div data-search-exclude markdown="1">



URI: [loc:FI-OL](https://w3id.org/lmodel/dpv/loc/FI-OL)





```mermaid
 classDiagram
    class FIOL
    click FIOL href "../FIOL/"
      FI <|-- FIOL
        click FI href "../FI/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FI](FI.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FIOL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FI-OL](https://w3id.org/lmodel/dpv/loc/FI-OL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FI-OL
* Oulu Province




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FI-OL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FI-OL |
| native | loc:FIOL |
| exact | dpv_loc:FI-OL, dpv_loc_owl:FI-OL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FIOL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FI-OL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Oulu Province in country Finland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FI-OL
- Oulu Province
exact_mappings:
- dpv_loc:FI-OL
- dpv_loc_owl:FI-OL
is_a: FI
class_uri: loc:FI-OL

```
</details>

### Induced

<details>
```yaml
name: FIOL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FI-OL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Oulu Province in country Finland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FI-OL
- Oulu Province
exact_mappings:
- dpv_loc:FI-OL
- dpv_loc_owl:FI-OL
is_a: FI
class_uri: loc:FI-OL

```
</details></div>