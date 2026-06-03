---
search:
  boost: 10.0
---

# Class: HUBA 


_Concept representing region Baranya County in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-BA](https://w3id.org/lmodel/dpv/loc/HU-BA)





```mermaid
 classDiagram
    class HUBA
    click HUBA href "../HUBA/"
      HU <|-- HUBA
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUBA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-BA](https://w3id.org/lmodel/dpv/loc/HU-BA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-BA
* Baranya County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-BA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-BA |
| native | loc:HUBA |
| exact | dpv_loc:HU-BA, dpv_loc_owl:HU-BA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUBA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-BA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Baranya County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-BA
- Baranya County
exact_mappings:
- dpv_loc:HU-BA
- dpv_loc_owl:HU-BA
is_a: HU
class_uri: loc:HU-BA

```
</details>

### Induced

<details>
```yaml
name: HUBA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-BA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Baranya County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-BA
- Baranya County
exact_mappings:
- dpv_loc:HU-BA
- dpv_loc_owl:HU-BA
is_a: HU
class_uri: loc:HU-BA

```
</details></div>