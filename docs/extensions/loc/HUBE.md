---
search:
  boost: 10.0
---

# Class: HUBE 


_Concept representing region Békés County in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-BE](https://w3id.org/lmodel/dpv/loc/HU-BE)





```mermaid
 classDiagram
    class HUBE
    click HUBE href "../HUBE/"
      HU <|-- HUBE
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUBE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-BE](https://w3id.org/lmodel/dpv/loc/HU-BE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-BE
* Békés County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-BE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-BE |
| native | loc:HUBE |
| exact | dpv_loc:HU-BE, dpv_loc_owl:HU-BE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUBE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-BE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Békés County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-BE
- Békés County
exact_mappings:
- dpv_loc:HU-BE
- dpv_loc_owl:HU-BE
is_a: HU
class_uri: loc:HU-BE

```
</details>

### Induced

<details>
```yaml
name: HUBE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-BE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Békés County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-BE
- Békés County
exact_mappings:
- dpv_loc:HU-BE
- dpv_loc_owl:HU-BE
is_a: HU
class_uri: loc:HU-BE

```
</details></div>