---
search:
  boost: 10.0
---

# Class: LUCA 


_Concept representing region Canton of Capellen in country Luxembourg_



<div data-search-exclude markdown="1">



URI: [loc:LU-CA](https://w3id.org/lmodel/dpv/loc/LU-CA)





```mermaid
 classDiagram
    class LUCA
    click LUCA href "../LUCA/"
      LU <|-- LUCA
        click LU href "../LU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LU](LU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LUCA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LU-CA](https://w3id.org/lmodel/dpv/loc/LU-CA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LU-CA
* Canton of Capellen




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LU-CA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LU-CA |
| native | loc:LUCA |
| exact | dpv_loc:LU-CA, dpv_loc_owl:LU-CA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LUCA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-CA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Capellen in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-CA
- Canton of Capellen
exact_mappings:
- dpv_loc:LU-CA
- dpv_loc_owl:LU-CA
is_a: LU
class_uri: loc:LU-CA

```
</details>

### Induced

<details>
```yaml
name: LUCA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-CA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Capellen in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-CA
- Canton of Capellen
exact_mappings:
- dpv_loc:LU-CA
- dpv_loc_owl:LU-CA
is_a: LU
class_uri: loc:LU-CA

```
</details></div>