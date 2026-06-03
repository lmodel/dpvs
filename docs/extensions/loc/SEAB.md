---
search:
  boost: 10.0
---

# Class: SEAB 


_Concept representing region Stockholm County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-AB](https://w3id.org/lmodel/dpv/loc/SE-AB)





```mermaid
 classDiagram
    class SEAB
    click SEAB href "../SEAB/"
      SE <|-- SEAB
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEAB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-AB](https://w3id.org/lmodel/dpv/loc/SE-AB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-AB
* Stockholm County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-AB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-AB |
| native | loc:SEAB |
| exact | dpv_loc:SE-AB, dpv_loc_owl:SE-AB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEAB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-AB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Stockholm County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-AB
- Stockholm County
exact_mappings:
- dpv_loc:SE-AB
- dpv_loc_owl:SE-AB
is_a: SE
class_uri: loc:SE-AB

```
</details>

### Induced

<details>
```yaml
name: SEAB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-AB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Stockholm County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-AB
- Stockholm County
exact_mappings:
- dpv_loc:SE-AB
- dpv_loc_owl:SE-AB
is_a: SE
class_uri: loc:SE-AB

```
</details></div>