---
search:
  boost: 10.0
---

# Class: LTAL 


_Concept representing region Alytus County in country Lithuania_



<div data-search-exclude markdown="1">



URI: [loc:LT-AL](https://w3id.org/lmodel/dpv/loc/LT-AL)





```mermaid
 classDiagram
    class LTAL
    click LTAL href "../LTAL/"
      LT <|-- LTAL
        click LT href "../LT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [LT](LT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **LTAL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LT-AL](https://w3id.org/lmodel/dpv/loc/LT-AL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* LT-AL
* Alytus County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LT-AL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LT-AL |
| native | loc:LTAL |
| exact | dpv_loc:LT-AL, dpv_loc_owl:LT-AL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LTAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LT-AL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Alytus County in country Lithuania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LT-AL
- Alytus County
exact_mappings:
- dpv_loc:LT-AL
- dpv_loc_owl:LT-AL
is_a: LT
class_uri: loc:LT-AL

```
</details>

### Induced

<details>
```yaml
name: LTAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LT-AL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Alytus County in country Lithuania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- LT-AL
- Alytus County
exact_mappings:
- dpv_loc:LT-AL
- dpv_loc_owl:LT-AL
is_a: LT
class_uri: loc:LT-AL

```
</details></div>