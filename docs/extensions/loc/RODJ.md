---
search:
  boost: 10.0
---

# Class: RODJ 


_Concept representing region Dolj County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-DJ](https://w3id.org/lmodel/dpv/loc/RO-DJ)





```mermaid
 classDiagram
    class RODJ
    click RODJ href "../RODJ/"
      RO <|-- RODJ
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **RODJ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-DJ](https://w3id.org/lmodel/dpv/loc/RO-DJ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-DJ
* Dolj County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-DJ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-DJ |
| native | loc:RODJ |
| exact | dpv_loc:RO-DJ, dpv_loc_owl:RO-DJ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RODJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-DJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dolj County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-DJ
- Dolj County
exact_mappings:
- dpv_loc:RO-DJ
- dpv_loc_owl:RO-DJ
is_a: RO
class_uri: loc:RO-DJ

```
</details>

### Induced

<details>
```yaml
name: RODJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-DJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dolj County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-DJ
- Dolj County
exact_mappings:
- dpv_loc:RO-DJ
- dpv_loc_owl:RO-DJ
is_a: RO
class_uri: loc:RO-DJ

```
</details></div>