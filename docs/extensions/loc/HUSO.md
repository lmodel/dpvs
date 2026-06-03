---
search:
  boost: 10.0
---

# Class: HUSO 


_Concept representing region Somogy County in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-SO](https://w3id.org/lmodel/dpv/loc/HU-SO)





```mermaid
 classDiagram
    class HUSO
    click HUSO href "../HUSO/"
      HU <|-- HUSO
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUSO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-SO](https://w3id.org/lmodel/dpv/loc/HU-SO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-SO
* Somogy County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-SO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-SO |
| native | loc:HUSO |
| exact | dpv_loc:HU-SO, dpv_loc_owl:HU-SO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUSO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Somogy County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SO
- Somogy County
exact_mappings:
- dpv_loc:HU-SO
- dpv_loc_owl:HU-SO
is_a: HU
class_uri: loc:HU-SO

```
</details>

### Induced

<details>
```yaml
name: HUSO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-SO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Somogy County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-SO
- Somogy County
exact_mappings:
- dpv_loc:HU-SO
- dpv_loc_owl:HU-SO
is_a: HU
class_uri: loc:HU-SO

```
</details></div>