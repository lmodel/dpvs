---
search:
  boost: 10.0
---

# Class: HUSN 


_Concept representing region Sopron in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-SN](https://w3id.org/lmodel/dpv/loc/HU-SN)





```mermaid
 classDiagram
    class HUSN
    click HUSN href "../HUSN/"
      HU <|-- HUSN
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUSN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-SN](https://w3id.org/lmodel/dpv/loc/HU-SN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-SN
* Sopron




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-SN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-SN |
| native | loc:HUSN |
| exact | dpv_loc:HU-SN, dpv_loc_owl:HU-SN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUSN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Sopron in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SN
- Sopron
exact_mappings:
- dpv_loc:HU-SN
- dpv_loc_owl:HU-SN
is_a: HU
class_uri: loc:HU-SN

```
</details>

### Induced

<details>
```yaml
name: HUSN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Sopron in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SN
- Sopron
exact_mappings:
- dpv_loc:HU-SN
- dpv_loc_owl:HU-SN
is_a: HU
class_uri: loc:HU-SN

```
</details></div>