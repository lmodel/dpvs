---
search:
  boost: 10.0
---

# Class: HUDE 


_Concept representing region Debrecen in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-DE](https://w3id.org/lmodel/dpv/loc/HU-DE)





```mermaid
 classDiagram
    class HUDE
    click HUDE href "../HUDE/"
      HU <|-- HUDE
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUDE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-DE](https://w3id.org/lmodel/dpv/loc/HU-DE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-DE
* Debrecen




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-DE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-DE |
| native | loc:HUDE |
| exact | dpv_loc:HU-DE, dpv_loc_owl:HU-DE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUDE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-DE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Debrecen in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-DE
- Debrecen
exact_mappings:
- dpv_loc:HU-DE
- dpv_loc_owl:HU-DE
is_a: HU
class_uri: loc:HU-DE

```
</details>

### Induced

<details>
```yaml
name: HUDE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-DE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Debrecen in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-DE
- Debrecen
exact_mappings:
- dpv_loc:HU-DE
- dpv_loc_owl:HU-DE
is_a: HU
class_uri: loc:HU-DE

```
</details></div>