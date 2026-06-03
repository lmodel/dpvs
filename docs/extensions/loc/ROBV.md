---
search:
  boost: 10.0
---

# Class: ROBV 


_Concept representing region Brașov County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-BV](https://w3id.org/lmodel/dpv/loc/RO-BV)





```mermaid
 classDiagram
    class ROBV
    click ROBV href "../ROBV/"
      RO <|-- ROBV
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROBV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-BV](https://w3id.org/lmodel/dpv/loc/RO-BV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-BV
* Brașov County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-BV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-BV |
| native | loc:ROBV |
| exact | dpv_loc:RO-BV, dpv_loc_owl:RO-BV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROBV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-BV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Brașov County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-BV
- Brașov County
exact_mappings:
- dpv_loc:RO-BV
- dpv_loc_owl:RO-BV
is_a: RO
class_uri: loc:RO-BV

```
</details>

### Induced

<details>
```yaml
name: ROBV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-BV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Brașov County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-BV
- Brașov County
exact_mappings:
- dpv_loc:RO-BV
- dpv_loc_owl:RO-BV
is_a: RO
class_uri: loc:RO-BV

```
</details></div>