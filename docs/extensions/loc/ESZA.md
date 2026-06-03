---
search:
  boost: 10.0
---

# Class: ESZA 


_Concept representing region Province of Zamora in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-ZA](https://w3id.org/lmodel/dpv/loc/ES-ZA)





```mermaid
 classDiagram
    class ESZA
    click ESZA href "../ESZA/"
      ES <|-- ESZA
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESZA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-ZA](https://w3id.org/lmodel/dpv/loc/ES-ZA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-ZA
* Province of Zamora




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-ZA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-ZA |
| native | loc:ESZA |
| exact | dpv_loc:ES-ZA, dpv_loc_owl:ES-ZA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESZA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-ZA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Zamora in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-ZA
- Province of Zamora
exact_mappings:
- dpv_loc:ES-ZA
- dpv_loc_owl:ES-ZA
is_a: ES
class_uri: loc:ES-ZA

```
</details>

### Induced

<details>
```yaml
name: ESZA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-ZA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Zamora in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-ZA
- Province of Zamora
exact_mappings:
- dpv_loc:ES-ZA
- dpv_loc_owl:ES-ZA
is_a: ES
class_uri: loc:ES-ZA

```
</details></div>