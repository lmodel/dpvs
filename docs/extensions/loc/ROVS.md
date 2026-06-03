---
search:
  boost: 10.0
---

# Class: ROVS 


_Concept representing region Vaslui County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-VS](https://w3id.org/lmodel/dpv/loc/RO-VS)





```mermaid
 classDiagram
    class ROVS
    click ROVS href "../ROVS/"
      RO <|-- ROVS
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROVS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-VS](https://w3id.org/lmodel/dpv/loc/RO-VS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-VS
* Vaslui County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-VS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-VS |
| native | loc:ROVS |
| exact | dpv_loc:RO-VS, dpv_loc_owl:RO-VS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROVS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-VS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vaslui County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-VS
- Vaslui County
exact_mappings:
- dpv_loc:RO-VS
- dpv_loc_owl:RO-VS
is_a: RO
class_uri: loc:RO-VS

```
</details>

### Induced

<details>
```yaml
name: ROVS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-VS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vaslui County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-VS
- Vaslui County
exact_mappings:
- dpv_loc:RO-VS
- dpv_loc_owl:RO-VS
is_a: RO
class_uri: loc:RO-VS

```
</details></div>