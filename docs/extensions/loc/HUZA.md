---
search:
  boost: 10.0
---

# Class: HUZA 


_Concept representing region Zala County in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-ZA](https://w3id.org/lmodel/dpv/loc/HU-ZA)





```mermaid
 classDiagram
    class HUZA
    click HUZA href "../HUZA/"
      HU <|-- HUZA
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUZA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-ZA](https://w3id.org/lmodel/dpv/loc/HU-ZA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-ZA
* Zala County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-ZA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-ZA |
| native | loc:HUZA |
| exact | dpv_loc:HU-ZA, dpv_loc_owl:HU-ZA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUZA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-ZA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Zala County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-ZA
- Zala County
exact_mappings:
- dpv_loc:HU-ZA
- dpv_loc_owl:HU-ZA
is_a: HU
class_uri: loc:HU-ZA

```
</details>

### Induced

<details>
```yaml
name: HUZA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-ZA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Zala County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-ZA
- Zala County
exact_mappings:
- dpv_loc:HU-ZA
- dpv_loc_owl:HU-ZA
is_a: HU
class_uri: loc:HU-ZA

```
</details></div>