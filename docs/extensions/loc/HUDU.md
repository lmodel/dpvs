---
search:
  boost: 10.0
---

# Class: HUDU 


_Concept representing region Dunaújváros in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-DU](https://w3id.org/lmodel/dpv/loc/HU-DU)





```mermaid
 classDiagram
    class HUDU
    click HUDU href "../HUDU/"
      HU <|-- HUDU
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUDU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-DU](https://w3id.org/lmodel/dpv/loc/HU-DU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-DU
* Dunaújváros




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-DU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-DU |
| native | loc:HUDU |
| exact | dpv_loc:HU-DU, dpv_loc_owl:HU-DU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUDU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-DU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dunaújváros in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-DU
- Dunaújváros
exact_mappings:
- dpv_loc:HU-DU
- dpv_loc_owl:HU-DU
is_a: HU
class_uri: loc:HU-DU

```
</details>

### Induced

<details>
```yaml
name: HUDU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-DU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dunaújváros in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-DU
- Dunaújváros
exact_mappings:
- dpv_loc:HU-DU
- dpv_loc_owl:HU-DU
is_a: HU
class_uri: loc:HU-DU

```
</details></div>