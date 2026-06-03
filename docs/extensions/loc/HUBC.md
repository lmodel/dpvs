---
search:
  boost: 10.0
---

# Class: HUBC 


_Concept representing region Békéscsaba in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-BC](https://w3id.org/lmodel/dpv/loc/HU-BC)





```mermaid
 classDiagram
    class HUBC
    click HUBC href "../HUBC/"
      HU <|-- HUBC
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUBC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-BC](https://w3id.org/lmodel/dpv/loc/HU-BC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-BC
* Békéscsaba




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-BC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-BC |
| native | loc:HUBC |
| exact | dpv_loc:HU-BC, dpv_loc_owl:HU-BC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUBC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-BC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Békéscsaba in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-BC
- Békéscsaba
exact_mappings:
- dpv_loc:HU-BC
- dpv_loc_owl:HU-BC
is_a: HU
class_uri: loc:HU-BC

```
</details>

### Induced

<details>
```yaml
name: HUBC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-BC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Békéscsaba in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-BC
- Békéscsaba
exact_mappings:
- dpv_loc:HU-BC
- dpv_loc_owl:HU-BC
is_a: HU
class_uri: loc:HU-BC

```
</details></div>