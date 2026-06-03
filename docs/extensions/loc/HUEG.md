---
search:
  boost: 10.0
---

# Class: HUEG 


_Concept representing region Eger in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-EG](https://w3id.org/lmodel/dpv/loc/HU-EG)





```mermaid
 classDiagram
    class HUEG
    click HUEG href "../HUEG/"
      HU <|-- HUEG
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUEG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-EG](https://w3id.org/lmodel/dpv/loc/HU-EG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-EG
* Eger




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-EG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-EG |
| native | loc:HUEG |
| exact | dpv_loc:HU-EG, dpv_loc_owl:HU-EG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUEG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-EG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Eger in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-EG
- Eger
exact_mappings:
- dpv_loc:HU-EG
- dpv_loc_owl:HU-EG
is_a: HU
class_uri: loc:HU-EG

```
</details>

### Induced

<details>
```yaml
name: HUEG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-EG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Eger in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-EG
- Eger
exact_mappings:
- dpv_loc:HU-EG
- dpv_loc_owl:HU-EG
is_a: HU
class_uri: loc:HU-EG

```
</details></div>