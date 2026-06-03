---
search:
  boost: 10.0
---

# Class: ROSM 


_Concept representing region Satu Mare County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-SM](https://w3id.org/lmodel/dpv/loc/RO-SM)





```mermaid
 classDiagram
    class ROSM
    click ROSM href "../ROSM/"
      RO <|-- ROSM
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROSM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-SM](https://w3id.org/lmodel/dpv/loc/RO-SM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-SM
* Satu Mare County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-SM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-SM |
| native | loc:ROSM |
| exact | dpv_loc:RO-SM, dpv_loc_owl:RO-SM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROSM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-SM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Satu Mare County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-SM
- Satu Mare County
exact_mappings:
- dpv_loc:RO-SM
- dpv_loc_owl:RO-SM
is_a: RO
class_uri: loc:RO-SM

```
</details>

### Induced

<details>
```yaml
name: ROSM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-SM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Satu Mare County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-SM
- Satu Mare County
exact_mappings:
- dpv_loc:RO-SM
- dpv_loc_owl:RO-SM
is_a: RO
class_uri: loc:RO-SM

```
</details></div>