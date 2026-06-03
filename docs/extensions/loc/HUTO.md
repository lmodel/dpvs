---
search:
  boost: 10.0
---

# Class: HUTO 


_Concept representing region Tolna County in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-TO](https://w3id.org/lmodel/dpv/loc/HU-TO)





```mermaid
 classDiagram
    class HUTO
    click HUTO href "../HUTO/"
      HU <|-- HUTO
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUTO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-TO](https://w3id.org/lmodel/dpv/loc/HU-TO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-TO
* Tolna County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-TO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-TO |
| native | loc:HUTO |
| exact | dpv_loc:HU-TO, dpv_loc_owl:HU-TO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUTO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-TO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Tolna County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-TO
- Tolna County
exact_mappings:
- dpv_loc:HU-TO
- dpv_loc_owl:HU-TO
is_a: HU
class_uri: loc:HU-TO

```
</details>

### Induced

<details>
```yaml
name: HUTO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-TO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Tolna County in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-TO
- Tolna County
exact_mappings:
- dpv_loc:HU-TO
- dpv_loc_owl:HU-TO
is_a: HU
class_uri: loc:HU-TO

```
</details></div>