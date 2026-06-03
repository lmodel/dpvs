---
search:
  boost: 10.0
---

# Class: HUNY 


_Concept representing region Nyíregyháza in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-NY](https://w3id.org/lmodel/dpv/loc/HU-NY)





```mermaid
 classDiagram
    class HUNY
    click HUNY href "../HUNY/"
      HU <|-- HUNY
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUNY**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-NY](https://w3id.org/lmodel/dpv/loc/HU-NY) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-NY
* Nyíregyháza




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-NY |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-NY |
| native | loc:HUNY |
| exact | dpv_loc:HU-NY, dpv_loc_owl:HU-NY |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUNY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-NY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nyíregyháza in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-NY
- Nyíregyháza
exact_mappings:
- dpv_loc:HU-NY
- dpv_loc_owl:HU-NY
is_a: HU
class_uri: loc:HU-NY

```
</details>

### Induced

<details>
```yaml
name: HUNY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-NY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nyíregyháza in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-NY
- Nyíregyháza
exact_mappings:
- dpv_loc:HU-NY
- dpv_loc_owl:HU-NY
is_a: HU
class_uri: loc:HU-NY

```
</details></div>