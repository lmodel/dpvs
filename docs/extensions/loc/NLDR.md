---
search:
  boost: 10.0
---

# Class: NLDR 


_Concept representing region Drenthe in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-DR](https://w3id.org/lmodel/dpv/loc/NL-DR)





```mermaid
 classDiagram
    class NLDR
    click NLDR href "../NLDR/"
      NL <|-- NLDR
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLDR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-DR](https://w3id.org/lmodel/dpv/loc/NL-DR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-DR
* Drenthe




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-DR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-DR |
| native | loc:NLDR |
| exact | dpv_loc:NL-DR, dpv_loc_owl:NL-DR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLDR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-DR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Drenthe in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-DR
- Drenthe
exact_mappings:
- dpv_loc:NL-DR
- dpv_loc_owl:NL-DR
is_a: NL
class_uri: loc:NL-DR

```
</details>

### Induced

<details>
```yaml
name: NLDR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-DR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Drenthe in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-DR
- Drenthe
exact_mappings:
- dpv_loc:NL-DR
- dpv_loc_owl:NL-DR
is_a: NL
class_uri: loc:NL-DR

```
</details></div>