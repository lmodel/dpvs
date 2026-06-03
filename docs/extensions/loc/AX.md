---
search:
  boost: 10.0
---

# Class: AX 


_Concept representing Country of Åland Islands_



<div data-search-exclude markdown="1">



URI: [loc:AX](https://w3id.org/lmodel/dpv/loc/AX)





```mermaid
 classDiagram
    class AX
    click AX href "../AX/"
      FI <|-- AX
        click FI href "../FI/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FI](FI.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **AX**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AX](https://w3id.org/lmodel/dpv/loc/AX) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Åland Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AX |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AX |
| native | loc:AX |
| exact | dpv_loc:AX, dpv_loc_owl:AX |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AX
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AX
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Åland Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Åland Islands
exact_mappings:
- dpv_loc:AX
- dpv_loc_owl:AX
is_a: FI
class_uri: loc:AX

```
</details>

### Induced

<details>
```yaml
name: AX
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AX
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Åland Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Åland Islands
exact_mappings:
- dpv_loc:AX
- dpv_loc_owl:AX
is_a: FI
class_uri: loc:AX

```
</details></div>