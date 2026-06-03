---
search:
  boost: 10.0
---

# Class: ROHR 


_Concept representing region Harghita County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-HR](https://w3id.org/lmodel/dpv/loc/RO-HR)





```mermaid
 classDiagram
    class ROHR
    click ROHR href "../ROHR/"
      RO <|-- ROHR
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROHR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-HR](https://w3id.org/lmodel/dpv/loc/RO-HR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-HR
* Harghita County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-HR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-HR |
| native | loc:ROHR |
| exact | dpv_loc:RO-HR, dpv_loc_owl:RO-HR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROHR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-HR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Harghita County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-HR
- Harghita County
exact_mappings:
- dpv_loc:RO-HR
- dpv_loc_owl:RO-HR
is_a: RO
class_uri: loc:RO-HR

```
</details>

### Induced

<details>
```yaml
name: ROHR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-HR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Harghita County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-HR
- Harghita County
exact_mappings:
- dpv_loc:RO-HR
- dpv_loc_owl:RO-HR
is_a: RO
class_uri: loc:RO-HR

```
</details></div>