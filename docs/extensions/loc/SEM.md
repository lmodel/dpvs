---
search:
  boost: 10.0
---

# Class: SEM 


_Concept representing region Skåne County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-M](https://w3id.org/lmodel/dpv/loc/SE-M)





```mermaid
 classDiagram
    class SEM
    click SEM href "../SEM/"
      SE <|-- SEM
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-M](https://w3id.org/lmodel/dpv/loc/SE-M) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-M
* Skåne County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-M |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-M |
| native | loc:SEM |
| exact | dpv_loc:SE-M, dpv_loc_owl:SE-M |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-M
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Skåne County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-M
- Skåne County
exact_mappings:
- dpv_loc:SE-M
- dpv_loc_owl:SE-M
is_a: SE
class_uri: loc:SE-M

```
</details>

### Induced

<details>
```yaml
name: SEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-M
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Skåne County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-M
- Skåne County
exact_mappings:
- dpv_loc:SE-M
- dpv_loc_owl:SE-M
is_a: SE
class_uri: loc:SE-M

```
</details></div>