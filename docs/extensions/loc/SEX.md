---
search:
  boost: 10.0
---

# Class: SEX 


_Concept representing region Gävleborg County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-X](https://w3id.org/lmodel/dpv/loc/SE-X)





```mermaid
 classDiagram
    class SEX
    click SEX href "../SEX/"
      SE <|-- SEX
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEX**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-X](https://w3id.org/lmodel/dpv/loc/SE-X) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-X
* Gävleborg County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-X |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-X |
| native | loc:SEX |
| exact | dpv_loc:SE-X, dpv_loc_owl:SE-X |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEX
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-X
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gävleborg County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-X
- Gävleborg County
exact_mappings:
- dpv_loc:SE-X
- dpv_loc_owl:SE-X
is_a: SE
class_uri: loc:SE-X

```
</details>

### Induced

<details>
```yaml
name: SEX
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-X
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gävleborg County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-X
- Gävleborg County
exact_mappings:
- dpv_loc:SE-X
- dpv_loc_owl:SE-X
is_a: SE
class_uri: loc:SE-X

```
</details></div>