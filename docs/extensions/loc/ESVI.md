---
search:
  boost: 10.0
---

# Class: ESVI 


_Concept representing region Álava-Araba in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-VI](https://w3id.org/lmodel/dpv/loc/ES-VI)





```mermaid
 classDiagram
    class ESVI
    click ESVI href "../ESVI/"
      ES <|-- ESVI
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESVI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-VI](https://w3id.org/lmodel/dpv/loc/ES-VI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-VI
* Álava-Araba




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-VI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-VI |
| native | loc:ESVI |
| exact | dpv_loc:ES-VI, dpv_loc_owl:ES-VI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESVI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-VI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Álava-Araba in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-VI
- Álava-Araba
exact_mappings:
- dpv_loc:ES-VI
- dpv_loc_owl:ES-VI
is_a: ES
class_uri: loc:ES-VI

```
</details>

### Induced

<details>
```yaml
name: ESVI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-VI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Álava-Araba in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-VI
- Álava-Araba
exact_mappings:
- dpv_loc:ES-VI
- dpv_loc_owl:ES-VI
is_a: ES
class_uri: loc:ES-VI

```
</details></div>