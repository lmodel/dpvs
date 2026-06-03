---
search:
  boost: 10.0
---

# Class: IECO 


_Concept representing region County Cork in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-CO](https://w3id.org/lmodel/dpv/loc/IE-CO)





```mermaid
 classDiagram
    class IECO
    click IECO href "../IECO/"
      IE <|-- IECO
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IECO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-CO](https://w3id.org/lmodel/dpv/loc/IE-CO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-CO
* County Cork




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-CO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-CO |
| native | loc:IECO |
| exact | dpv_loc:IE-CO, dpv_loc_owl:IE-CO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IECO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-CO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Cork in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-CO
- County Cork
exact_mappings:
- dpv_loc:IE-CO
- dpv_loc_owl:IE-CO
is_a: IE
class_uri: loc:IE-CO

```
</details>

### Induced

<details>
```yaml
name: IECO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-CO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Cork in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-CO
- County Cork
exact_mappings:
- dpv_loc:IE-CO
- dpv_loc_owl:IE-CO
is_a: IE
class_uri: loc:IE-CO

```
</details></div>