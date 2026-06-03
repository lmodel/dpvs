---
search:
  boost: 10.0
---

# Class: ROSV 


_Concept representing region Suceava County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-SV](https://w3id.org/lmodel/dpv/loc/RO-SV)





```mermaid
 classDiagram
    class ROSV
    click ROSV href "../ROSV/"
      RO <|-- ROSV
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROSV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-SV](https://w3id.org/lmodel/dpv/loc/RO-SV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-SV
* Suceava County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-SV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-SV |
| native | loc:ROSV |
| exact | dpv_loc:RO-SV, dpv_loc_owl:RO-SV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROSV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-SV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Suceava County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-SV
- Suceava County
exact_mappings:
- dpv_loc:RO-SV
- dpv_loc_owl:RO-SV
is_a: RO
class_uri: loc:RO-SV

```
</details>

### Induced

<details>
```yaml
name: ROSV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-SV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Suceava County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-SV
- Suceava County
exact_mappings:
- dpv_loc:RO-SV
- dpv_loc_owl:RO-SV
is_a: RO
class_uri: loc:RO-SV

```
</details></div>