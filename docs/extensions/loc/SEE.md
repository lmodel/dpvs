---
search:
  boost: 10.0
---

# Class: SEE 


_Concept representing region Östergötland County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-E](https://w3id.org/lmodel/dpv/loc/SE-E)





```mermaid
 classDiagram
    class SEE
    click SEE href "../SEE/"
      SE <|-- SEE
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-E](https://w3id.org/lmodel/dpv/loc/SE-E) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-E
* Östergötland County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-E |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-E |
| native | loc:SEE |
| exact | dpv_loc:SE-E, dpv_loc_owl:SE-E |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-E
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Östergötland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-E
- Östergötland County
exact_mappings:
- dpv_loc:SE-E
- dpv_loc_owl:SE-E
is_a: SE
class_uri: loc:SE-E

```
</details>

### Induced

<details>
```yaml
name: SEE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-E
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Östergötland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-E
- Östergötland County
exact_mappings:
- dpv_loc:SE-E
- dpv_loc_owl:SE-E
is_a: SE
class_uri: loc:SE-E

```
</details></div>