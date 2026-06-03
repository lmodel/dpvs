---
search:
  boost: 10.0
---

# Class: HUSS 


_Concept representing region Szekszárd in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-SS](https://w3id.org/lmodel/dpv/loc/HU-SS)





```mermaid
 classDiagram
    class HUSS
    click HUSS href "../HUSS/"
      HU <|-- HUSS
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUSS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-SS](https://w3id.org/lmodel/dpv/loc/HU-SS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-SS
* Szekszárd




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-SS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-SS |
| native | loc:HUSS |
| exact | dpv_loc:HU-SS, dpv_loc_owl:HU-SS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUSS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Szekszárd in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SS
- Szekszárd
exact_mappings:
- dpv_loc:HU-SS
- dpv_loc_owl:HU-SS
is_a: HU
class_uri: loc:HU-SS

```
</details>

### Induced

<details>
```yaml
name: HUSS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Szekszárd in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SS
- Szekszárd
exact_mappings:
- dpv_loc:HU-SS
- dpv_loc_owl:HU-SS
is_a: HU
class_uri: loc:HU-SS

```
</details></div>