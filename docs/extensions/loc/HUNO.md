---
search:
  boost: 10.0
---

# Class: HUNO 


_Concept representing region Nógrád County in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-NO](https://w3id.org/lmodel/dpv/loc/HU-NO)





```mermaid
 classDiagram
    class HUNO
    click HUNO href "../HUNO/"
      HU <|-- HUNO
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUNO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-NO](https://w3id.org/lmodel/dpv/loc/HU-NO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-NO
* Nógrád County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-NO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-NO |
| native | loc:HUNO |
| exact | dpv_loc:HU-NO, dpv_loc_owl:HU-NO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUNO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-NO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nógrád County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-NO
- Nógrád County
exact_mappings:
- dpv_loc:HU-NO
- dpv_loc_owl:HU-NO
is_a: HU
class_uri: loc:HU-NO

```
</details>

### Induced

<details>
```yaml
name: HUNO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-NO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nógrád County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-NO
- Nógrád County
exact_mappings:
- dpv_loc:HU-NO
- dpv_loc_owl:HU-NO
is_a: HU
class_uri: loc:HU-NO

```
</details></div>