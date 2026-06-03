---
search:
  boost: 10.0
---

# Class: LUEC 


_Concept representing region Canton of Echternach in country Luxembourg_



<div data-search-exclude markdown="1">



URI: [loc:LU-EC](https://w3id.org/lmodel/dpv/loc/LU-EC)





```mermaid
 classDiagram
    class LUEC
    click LUEC href "../LUEC/"
      LU <|-- LUEC
        click LU href "../LU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LU](LU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LUEC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LU-EC](https://w3id.org/lmodel/dpv/loc/LU-EC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LU-EC
* Canton of Echternach




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LU-EC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LU-EC |
| native | loc:LUEC |
| exact | dpv_loc:LU-EC, dpv_loc_owl:LU-EC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LUEC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-EC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Echternach in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-EC
- Canton of Echternach
exact_mappings:
- dpv_loc:LU-EC
- dpv_loc_owl:LU-EC
is_a: LU
class_uri: loc:LU-EC

```
</details>

### Induced

<details>
```yaml
name: LUEC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LU-EC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canton of Echternach in country Luxembourg
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LU-EC
- Canton of Echternach
exact_mappings:
- dpv_loc:LU-EC
- dpv_loc_owl:LU-EC
is_a: LU
class_uri: loc:LU-EC

```
</details></div>