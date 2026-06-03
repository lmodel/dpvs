---
search:
  boost: 10.0
---

# Class: ROIL 


_Concept representing region Ialomița County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-IL](https://w3id.org/lmodel/dpv/loc/RO-IL)





```mermaid
 classDiagram
    class ROIL
    click ROIL href "../ROIL/"
      RO <|-- ROIL
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROIL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-IL](https://w3id.org/lmodel/dpv/loc/RO-IL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-IL
* Ialomița County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-IL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-IL |
| native | loc:ROIL |
| exact | dpv_loc:RO-IL, dpv_loc_owl:RO-IL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROIL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-IL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ialomița County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-IL
- Ialomița County
exact_mappings:
- dpv_loc:RO-IL
- dpv_loc_owl:RO-IL
is_a: RO
class_uri: loc:RO-IL

```
</details>

### Induced

<details>
```yaml
name: ROIL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-IL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ialomița County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-IL
- Ialomița County
exact_mappings:
- dpv_loc:RO-IL
- dpv_loc_owl:RO-IL
is_a: RO
class_uri: loc:RO-IL

```
</details></div>