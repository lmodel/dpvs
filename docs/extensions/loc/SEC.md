---
search:
  boost: 10.0
---

# Class: SEC 


_Concept representing region Uppsala County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-C](https://w3id.org/lmodel/dpv/loc/SE-C)





```mermaid
 classDiagram
    class SEC
    click SEC href "../SEC/"
      SE <|-- SEC
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-C](https://w3id.org/lmodel/dpv/loc/SE-C) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-C
* Uppsala County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-C |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-C |
| native | loc:SEC |
| exact | dpv_loc:SE-C, dpv_loc_owl:SE-C |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Uppsala County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-C
- Uppsala County
exact_mappings:
- dpv_loc:SE-C
- dpv_loc_owl:SE-C
is_a: SE
class_uri: loc:SE-C

```
</details>

### Induced

<details>
```yaml
name: SEC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Uppsala County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-C
- Uppsala County
exact_mappings:
- dpv_loc:SE-C
- dpv_loc_owl:SE-C
is_a: SE
class_uri: loc:SE-C

```
</details></div>