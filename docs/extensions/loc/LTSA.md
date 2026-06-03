---
search:
  boost: 10.0
---

# Class: LTSA 


_Concept representing region Šiauliai County in country Lithuania_



<div data-search-exclude markdown="1">



URI: [loc:LT-SA](https://w3id.org/lmodel/dpv/loc/LT-SA)





```mermaid
 classDiagram
    class LTSA
    click LTSA href "../LTSA/"
      LT <|-- LTSA
        click LT href "../LT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LT](LT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LTSA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LT-SA](https://w3id.org/lmodel/dpv/loc/LT-SA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LT-SA
* Šiauliai County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LT-SA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LT-SA |
| native | loc:LTSA |
| exact | dpv_loc:LT-SA, dpv_loc_owl:LT-SA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LTSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LT-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Šiauliai County in country Lithuania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LT-SA
- Šiauliai County
exact_mappings:
- dpv_loc:LT-SA
- dpv_loc_owl:LT-SA
is_a: LT
class_uri: loc:LT-SA

```
</details>

### Induced

<details>
```yaml
name: LTSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LT-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Šiauliai County in country Lithuania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LT-SA
- Šiauliai County
exact_mappings:
- dpv_loc:LT-SA
- dpv_loc_owl:LT-SA
is_a: LT
class_uri: loc:LT-SA

```
</details></div>