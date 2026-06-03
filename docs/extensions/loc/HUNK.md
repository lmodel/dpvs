---
search:
  boost: 10.0
---

# Class: HUNK 


_Concept representing region Nagykanizsa in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-NK](https://w3id.org/lmodel/dpv/loc/HU-NK)





```mermaid
 classDiagram
    class HUNK
    click HUNK href "../HUNK/"
      HU <|-- HUNK
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUNK**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-NK](https://w3id.org/lmodel/dpv/loc/HU-NK) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-NK
* Nagykanizsa




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-NK |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-NK |
| native | loc:HUNK |
| exact | dpv_loc:HU-NK, dpv_loc_owl:HU-NK |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUNK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-NK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nagykanizsa in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-NK
- Nagykanizsa
exact_mappings:
- dpv_loc:HU-NK
- dpv_loc_owl:HU-NK
is_a: HU
class_uri: loc:HU-NK

```
</details>

### Induced

<details>
```yaml
name: HUNK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-NK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nagykanizsa in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-NK
- Nagykanizsa
exact_mappings:
- dpv_loc:HU-NK
- dpv_loc_owl:HU-NK
is_a: HU
class_uri: loc:HU-NK

```
</details></div>