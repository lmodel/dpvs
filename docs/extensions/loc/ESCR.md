---
search:
  boost: 10.0
---

# Class: ESCR 


_Concept representing region Province of Ciudad Real in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CR](https://w3id.org/lmodel/dpv/loc/ES-CR)





```mermaid
 classDiagram
    class ESCR
    click ESCR href "../ESCR/"
      ES <|-- ESCR
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CR](https://w3id.org/lmodel/dpv/loc/ES-CR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CR
* Province of Ciudad Real




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CR |
| native | loc:ESCR |
| exact | dpv_loc:ES-CR, dpv_loc_owl:ES-CR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ciudad Real in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CR
- Province of Ciudad Real
exact_mappings:
- dpv_loc:ES-CR
- dpv_loc_owl:ES-CR
is_a: ES
class_uri: loc:ES-CR

```
</details>

### Induced

<details>
```yaml
name: ESCR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ciudad Real in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CR
- Province of Ciudad Real
exact_mappings:
- dpv_loc:ES-CR
- dpv_loc_owl:ES-CR
is_a: ES
class_uri: loc:ES-CR

```
</details></div>