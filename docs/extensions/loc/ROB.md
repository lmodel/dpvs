---
search:
  boost: 10.0
---

# Class: ROB 


_Concept representing region Bucharest in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-B](https://w3id.org/lmodel/dpv/loc/RO-B)





```mermaid
 classDiagram
    class ROB
    click ROB href "../ROB/"
      RO <|-- ROB
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-B](https://w3id.org/lmodel/dpv/loc/RO-B) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-B
* Bucharest




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-B |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-B |
| native | loc:ROB |
| exact | dpv_loc:RO-B, dpv_loc_owl:RO-B |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-B
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bucharest in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-B
- Bucharest
exact_mappings:
- dpv_loc:RO-B
- dpv_loc_owl:RO-B
is_a: RO
class_uri: loc:RO-B

```
</details>

### Induced

<details>
```yaml
name: ROB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-B
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bucharest in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-B
- Bucharest
exact_mappings:
- dpv_loc:RO-B
- dpv_loc_owl:RO-B
is_a: RO
class_uri: loc:RO-B

```
</details></div>