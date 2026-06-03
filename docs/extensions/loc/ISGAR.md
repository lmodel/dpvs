---
search:
  boost: 10.0
---

# Class: ISGAR 


_Concept representing region Garðabær in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-GAR](https://w3id.org/lmodel/dpv/loc/IS-GAR)





```mermaid
 classDiagram
    class ISGAR
    click ISGAR href "../ISGAR/"
      IS <|-- ISGAR
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISGAR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-GAR](https://w3id.org/lmodel/dpv/loc/IS-GAR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-GAR
* Garðabær




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-GAR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-GAR |
| native | loc:ISGAR |
| exact | dpv_loc:IS-GAR, dpv_loc_owl:IS-GAR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISGAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-GAR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Garðabær in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-GAR
- Garðabær
exact_mappings:
- dpv_loc:IS-GAR
- dpv_loc_owl:IS-GAR
is_a: IS
class_uri: loc:IS-GAR

```
</details>

### Induced

<details>
```yaml
name: ISGAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-GAR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Garðabær in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-GAR
- Garðabær
exact_mappings:
- dpv_loc:IS-GAR
- dpv_loc_owl:IS-GAR
is_a: IS
class_uri: loc:IS-GAR

```
</details></div>