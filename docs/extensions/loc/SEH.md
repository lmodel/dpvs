---
search:
  boost: 10.0
---

# Class: SEH 


_Concept representing region Kalmar County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-H](https://w3id.org/lmodel/dpv/loc/SE-H)





```mermaid
 classDiagram
    class SEH
    click SEH href "../SEH/"
      SE <|-- SEH
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-H](https://w3id.org/lmodel/dpv/loc/SE-H) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-H
* Kalmar County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-H |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-H |
| native | loc:SEH |
| exact | dpv_loc:SE-H, dpv_loc_owl:SE-H |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-H
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kalmar County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-H
- Kalmar County
exact_mappings:
- dpv_loc:SE-H
- dpv_loc_owl:SE-H
is_a: SE
class_uri: loc:SE-H

```
</details>

### Induced

<details>
```yaml
name: SEH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-H
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kalmar County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-H
- Kalmar County
exact_mappings:
- dpv_loc:SE-H
- dpv_loc_owl:SE-H
is_a: SE
class_uri: loc:SE-H

```
</details></div>