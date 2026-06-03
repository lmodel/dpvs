---
search:
  boost: 10.0
---

# Class: ESGR 


_Concept representing region Province of Granada in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-GR](https://w3id.org/lmodel/dpv/loc/ES-GR)





```mermaid
 classDiagram
    class ESGR
    click ESGR href "../ESGR/"
      ES <|-- ESGR
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESGR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-GR](https://w3id.org/lmodel/dpv/loc/ES-GR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-GR
* Province of Granada




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-GR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-GR |
| native | loc:ESGR |
| exact | dpv_loc:ES-GR, dpv_loc_owl:ES-GR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESGR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-GR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Granada in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-GR
- Province of Granada
exact_mappings:
- dpv_loc:ES-GR
- dpv_loc_owl:ES-GR
is_a: ES
class_uri: loc:ES-GR

```
</details>

### Induced

<details>
```yaml
name: ESGR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-GR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Granada in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-GR
- Province of Granada
exact_mappings:
- dpv_loc:ES-GR
- dpv_loc_owl:ES-GR
is_a: ES
class_uri: loc:ES-GR

```
</details></div>