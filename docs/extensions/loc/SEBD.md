---
search:
  boost: 10.0
---

# Class: SEBD 


_Concept representing region Norrbotten County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-BD](https://w3id.org/lmodel/dpv/loc/SE-BD)





```mermaid
 classDiagram
    class SEBD
    click SEBD href "../SEBD/"
      SE <|-- SEBD
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEBD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-BD](https://w3id.org/lmodel/dpv/loc/SE-BD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-BD
* Norrbotten County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-BD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-BD |
| native | loc:SEBD |
| exact | dpv_loc:SE-BD, dpv_loc_owl:SE-BD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEBD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-BD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Norrbotten County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-BD
- Norrbotten County
exact_mappings:
- dpv_loc:SE-BD
- dpv_loc_owl:SE-BD
is_a: SE
class_uri: loc:SE-BD

```
</details>

### Induced

<details>
```yaml
name: SEBD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-BD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Norrbotten County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-BD
- Norrbotten County
exact_mappings:
- dpv_loc:SE-BD
- dpv_loc_owl:SE-BD
is_a: SE
class_uri: loc:SE-BD

```
</details></div>