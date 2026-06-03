---
search:
  boost: 10.0
---

# Class: HUVE 


_Concept representing region Veszprém County in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-VE](https://w3id.org/lmodel/dpv/loc/HU-VE)





```mermaid
 classDiagram
    class HUVE
    click HUVE href "../HUVE/"
      HU <|-- HUVE
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUVE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-VE](https://w3id.org/lmodel/dpv/loc/HU-VE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-VE
* Veszprém County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-VE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-VE |
| native | loc:HUVE |
| exact | dpv_loc:HU-VE, dpv_loc_owl:HU-VE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUVE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-VE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Veszprém County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-VE
- Veszprém County
exact_mappings:
- dpv_loc:HU-VE
- dpv_loc_owl:HU-VE
is_a: HU
class_uri: loc:HU-VE

```
</details>

### Induced

<details>
```yaml
name: HUVE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-VE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Veszprém County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-VE
- Veszprém County
exact_mappings:
- dpv_loc:HU-VE
- dpv_loc_owl:HU-VE
is_a: HU
class_uri: loc:HU-VE

```
</details></div>