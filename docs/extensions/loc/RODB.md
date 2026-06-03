---
search:
  boost: 10.0
---

# Class: RODB 


_Concept representing region Dâmbovița County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-DB](https://w3id.org/lmodel/dpv/loc/RO-DB)





```mermaid
 classDiagram
    class RODB
    click RODB href "../RODB/"
      RO <|-- RODB
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **RODB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-DB](https://w3id.org/lmodel/dpv/loc/RO-DB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-DB
* Dâmbovița County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-DB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-DB |
| native | loc:RODB |
| exact | dpv_loc:RO-DB, dpv_loc_owl:RO-DB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RODB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-DB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dâmbovița County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-DB
- Dâmbovița County
exact_mappings:
- dpv_loc:RO-DB
- dpv_loc_owl:RO-DB
is_a: RO
class_uri: loc:RO-DB

```
</details>

### Induced

<details>
```yaml
name: RODB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-DB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dâmbovița County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-DB
- Dâmbovița County
exact_mappings:
- dpv_loc:RO-DB
- dpv_loc_owl:RO-DB
is_a: RO
class_uri: loc:RO-DB

```
</details></div>