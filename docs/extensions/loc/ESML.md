---
search:
  boost: 10.0
---

# Class: ESML 


_Concept representing region Melilla in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-ML](https://w3id.org/lmodel/dpv/loc/ES-ML)





```mermaid
 classDiagram
    class ESML
    click ESML href "../ESML/"
      ES <|-- ESML
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESML**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-ML](https://w3id.org/lmodel/dpv/loc/ES-ML) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-ML
* Melilla




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-ML |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-ML |
| native | loc:ESML |
| exact | dpv_loc:ES-ML, dpv_loc_owl:ES-ML |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESML
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-ML
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Melilla in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-ML
- Melilla
exact_mappings:
- dpv_loc:ES-ML
- dpv_loc_owl:ES-ML
is_a: ES
class_uri: loc:ES-ML

```
</details>

### Induced

<details>
```yaml
name: ESML
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-ML
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Melilla in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-ML
- Melilla
exact_mappings:
- dpv_loc:ES-ML
- dpv_loc_owl:ES-ML
is_a: ES
class_uri: loc:ES-ML

```
</details></div>