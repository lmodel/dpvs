---
search:
  boost: 10.0
---

# Class: ESCE 


_Concept representing region Ceuta in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CE](https://w3id.org/lmodel/dpv/loc/ES-CE)





```mermaid
 classDiagram
    class ESCE
    click ESCE href "../ESCE/"
      ES <|-- ESCE
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CE](https://w3id.org/lmodel/dpv/loc/ES-CE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CE
* Ceuta




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CE |
| native | loc:ESCE |
| exact | dpv_loc:ES-CE, dpv_loc_owl:ES-CE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ceuta in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CE
- Ceuta
exact_mappings:
- dpv_loc:ES-CE
- dpv_loc_owl:ES-CE
is_a: ES
class_uri: loc:ES-CE

```
</details>

### Induced

<details>
```yaml
name: ESCE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ceuta in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CE
- Ceuta
exact_mappings:
- dpv_loc:ES-CE
- dpv_loc_owl:ES-CE
is_a: ES
class_uri: loc:ES-CE

```
</details></div>