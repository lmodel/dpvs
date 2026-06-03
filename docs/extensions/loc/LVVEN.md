---
search:
  boost: 10.0
---

# Class: LVVEN 


_Concept representing region Ventspils in country Latvia_



<div data-search-exclude markdown="1">



URI: [loc:LV-VEN](https://w3id.org/lmodel/dpv/loc/LV-VEN)





```mermaid
 classDiagram
    class LVVEN
    click LVVEN href "../LVVEN/"
      LV <|-- LVVEN
        click LV href "../LV/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LV](LV.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LVVEN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LV-VEN](https://w3id.org/lmodel/dpv/loc/LV-VEN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LV-VEN
* Ventspils




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LV-VEN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LV-VEN |
| native | loc:LVVEN |
| exact | dpv_loc:LV-VEN, dpv_loc_owl:LV-VEN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LVVEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LV-VEN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ventspils in country Latvia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LV-VEN
- Ventspils
exact_mappings:
- dpv_loc:LV-VEN
- dpv_loc_owl:LV-VEN
is_a: LV
class_uri: loc:LV-VEN

```
</details>

### Induced

<details>
```yaml
name: LVVEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LV-VEN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ventspils in country Latvia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LV-VEN
- Ventspils
exact_mappings:
- dpv_loc:LV-VEN
- dpv_loc_owl:LV-VEN
is_a: LV
class_uri: loc:LV-VEN

```
</details></div>