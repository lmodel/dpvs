---
search:
  boost: 10.0
---

# Class: FRNAQ 


_Concept representing region Nouvelle-Aquitaine in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-NAQ](https://w3id.org/lmodel/dpv/loc/FR-NAQ)





```mermaid
 classDiagram
    class FRNAQ
    click FRNAQ href "../FRNAQ/"
      FR <|-- FRNAQ
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRNAQ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-NAQ](https://w3id.org/lmodel/dpv/loc/FR-NAQ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-NAQ
* Nouvelle-Aquitaine




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-NAQ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-NAQ |
| native | loc:FRNAQ |
| exact | dpv_loc:FR-NAQ, dpv_loc_owl:FR-NAQ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRNAQ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-NAQ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nouvelle-Aquitaine in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-NAQ
- Nouvelle-Aquitaine
exact_mappings:
- dpv_loc:FR-NAQ
- dpv_loc_owl:FR-NAQ
is_a: FR
class_uri: loc:FR-NAQ

```
</details>

### Induced

<details>
```yaml
name: FRNAQ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-NAQ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nouvelle-Aquitaine in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-NAQ
- Nouvelle-Aquitaine
exact_mappings:
- dpv_loc:FR-NAQ
- dpv_loc_owl:FR-NAQ
is_a: FR
class_uri: loc:FR-NAQ

```
</details></div>