---
search:
  boost: 10.0
---

# Class: HUBU 


_Concept representing region Budapest in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-BU](https://w3id.org/lmodel/dpv/loc/HU-BU)





```mermaid
 classDiagram
    class HUBU
    click HUBU href "../HUBU/"
      HU <|-- HUBU
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUBU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-BU](https://w3id.org/lmodel/dpv/loc/HU-BU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-BU
* Budapest




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-BU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-BU |
| native | loc:HUBU |
| exact | dpv_loc:HU-BU, dpv_loc_owl:HU-BU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUBU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-BU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Budapest in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-BU
- Budapest
exact_mappings:
- dpv_loc:HU-BU
- dpv_loc_owl:HU-BU
is_a: HU
class_uri: loc:HU-BU

```
</details>

### Induced

<details>
```yaml
name: HUBU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-BU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Budapest in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-BU
- Budapest
exact_mappings:
- dpv_loc:HU-BU
- dpv_loc_owl:HU-BU
is_a: HU
class_uri: loc:HU-BU

```
</details></div>