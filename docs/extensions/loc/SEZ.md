---
search:
  boost: 10.0
---

# Class: SEZ 


_Concept representing region Jämtland County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-Z](https://w3id.org/lmodel/dpv/loc/SE-Z)





```mermaid
 classDiagram
    class SEZ
    click SEZ href "../SEZ/"
      SE <|-- SEZ
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEZ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-Z](https://w3id.org/lmodel/dpv/loc/SE-Z) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-Z
* Jämtland County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-Z |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-Z |
| native | loc:SEZ |
| exact | dpv_loc:SE-Z, dpv_loc_owl:SE-Z |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-Z
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Jämtland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-Z
- Jämtland County
exact_mappings:
- dpv_loc:SE-Z
- dpv_loc_owl:SE-Z
is_a: SE
class_uri: loc:SE-Z

```
</details>

### Induced

<details>
```yaml
name: SEZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-Z
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Jämtland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-Z
- Jämtland County
exact_mappings:
- dpv_loc:SE-Z
- dpv_loc_owl:SE-Z
is_a: SE
class_uri: loc:SE-Z

```
</details></div>