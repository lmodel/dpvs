---
search:
  boost: 10.0
---

# Class: ESAN 


_Concept representing region Andalusia in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-AN](https://w3id.org/lmodel/dpv/loc/ES-AN)





```mermaid
 classDiagram
    class ESAN
    click ESAN href "../ESAN/"
      ES <|-- ESAN
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESAN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-AN](https://w3id.org/lmodel/dpv/loc/ES-AN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-AN
* Andalusia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-AN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-AN |
| native | loc:ESAN |
| exact | dpv_loc:ES-AN, dpv_loc_owl:ES-AN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Andalusia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AN
- Andalusia
exact_mappings:
- dpv_loc:ES-AN
- dpv_loc_owl:ES-AN
is_a: ES
class_uri: loc:ES-AN

```
</details>

### Induced

<details>
```yaml
name: ESAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Andalusia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AN
- Andalusia
exact_mappings:
- dpv_loc:ES-AN
- dpv_loc_owl:ES-AN
is_a: ES
class_uri: loc:ES-AN

```
</details></div>