---
search:
  boost: 10.0
---

# Class: ESCM 


_Concept representing region Castile-La Mancha in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CM](https://w3id.org/lmodel/dpv/loc/ES-CM)





```mermaid
 classDiagram
    class ESCM
    click ESCM href "../ESCM/"
      ES <|-- ESCM
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CM](https://w3id.org/lmodel/dpv/loc/ES-CM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CM
* Castile-La Mancha




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CM |
| native | loc:ESCM |
| exact | dpv_loc:ES-CM, dpv_loc_owl:ES-CM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Castile-La Mancha in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CM
- Castile-La Mancha
exact_mappings:
- dpv_loc:ES-CM
- dpv_loc_owl:ES-CM
is_a: ES
class_uri: loc:ES-CM

```
</details>

### Induced

<details>
```yaml
name: ESCM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Castile-La Mancha in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CM
- Castile-La Mancha
exact_mappings:
- dpv_loc:ES-CM
- dpv_loc_owl:ES-CM
is_a: ES
class_uri: loc:ES-CM

```
</details></div>