---
search:
  boost: 10.0
---

# Class: ROCV 


_Concept representing region Covasna County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-CV](https://w3id.org/lmodel/dpv/loc/RO-CV)





```mermaid
 classDiagram
    class ROCV
    click ROCV href "../ROCV/"
      RO <|-- ROCV
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROCV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-CV](https://w3id.org/lmodel/dpv/loc/RO-CV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-CV
* Covasna County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-CV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-CV |
| native | loc:ROCV |
| exact | dpv_loc:RO-CV, dpv_loc_owl:RO-CV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROCV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-CV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Covasna County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-CV
- Covasna County
exact_mappings:
- dpv_loc:RO-CV
- dpv_loc_owl:RO-CV
is_a: RO
class_uri: loc:RO-CV

```
</details>

### Induced

<details>
```yaml
name: ROCV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-CV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Covasna County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-CV
- Covasna County
exact_mappings:
- dpv_loc:RO-CV
- dpv_loc_owl:RO-CV
is_a: RO
class_uri: loc:RO-CV

```
</details></div>