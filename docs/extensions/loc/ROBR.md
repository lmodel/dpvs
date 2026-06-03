---
search:
  boost: 10.0
---

# Class: ROBR 


_Concept representing region Brăila County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-BR](https://w3id.org/lmodel/dpv/loc/RO-BR)





```mermaid
 classDiagram
    class ROBR
    click ROBR href "../ROBR/"
      RO <|-- ROBR
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROBR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-BR](https://w3id.org/lmodel/dpv/loc/RO-BR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-BR
* Brăila County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-BR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-BR |
| native | loc:ROBR |
| exact | dpv_loc:RO-BR, dpv_loc_owl:RO-BR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROBR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-BR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Brăila County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-BR
- Brăila County
exact_mappings:
- dpv_loc:RO-BR
- dpv_loc_owl:RO-BR
is_a: RO
class_uri: loc:RO-BR

```
</details>

### Induced

<details>
```yaml
name: ROBR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-BR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Brăila County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-BR
- Brăila County
exact_mappings:
- dpv_loc:RO-BR
- dpv_loc_owl:RO-BR
is_a: RO
class_uri: loc:RO-BR

```
</details></div>