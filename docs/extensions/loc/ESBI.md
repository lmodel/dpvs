---
search:
  boost: 10.0
---

# Class: ESBI 


_Concept representing region Biscay in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-BI](https://w3id.org/lmodel/dpv/loc/ES-BI)





```mermaid
 classDiagram
    class ESBI
    click ESBI href "../ESBI/"
      ES <|-- ESBI
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESBI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-BI](https://w3id.org/lmodel/dpv/loc/ES-BI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-BI
* Biscay




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-BI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-BI |
| native | loc:ESBI |
| exact | dpv_loc:ES-BI, dpv_loc_owl:ES-BI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESBI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-BI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Biscay in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-BI
- Biscay
exact_mappings:
- dpv_loc:ES-BI
- dpv_loc_owl:ES-BI
is_a: ES
class_uri: loc:ES-BI

```
</details>

### Induced

<details>
```yaml
name: ESBI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-BI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Biscay in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-BI
- Biscay
exact_mappings:
- dpv_loc:ES-BI
- dpv_loc_owl:ES-BI
is_a: ES
class_uri: loc:ES-BI

```
</details></div>