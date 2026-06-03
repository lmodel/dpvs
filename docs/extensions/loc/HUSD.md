---
search:
  boost: 10.0
---

# Class: HUSD 


_Concept representing region Szeged in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-SD](https://w3id.org/lmodel/dpv/loc/HU-SD)





```mermaid
 classDiagram
    class HUSD
    click HUSD href "../HUSD/"
      HU <|-- HUSD
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUSD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-SD](https://w3id.org/lmodel/dpv/loc/HU-SD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-SD
* Szeged




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-SD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-SD |
| native | loc:HUSD |
| exact | dpv_loc:HU-SD, dpv_loc_owl:HU-SD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUSD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Szeged in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SD
- Szeged
exact_mappings:
- dpv_loc:HU-SD
- dpv_loc_owl:HU-SD
is_a: HU
class_uri: loc:HU-SD

```
</details>

### Induced

<details>
```yaml
name: HUSD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Szeged in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SD
- Szeged
exact_mappings:
- dpv_loc:HU-SD
- dpv_loc_owl:HU-SD
is_a: HU
class_uri: loc:HU-SD

```
</details></div>