---
search:
  boost: 10.0
---

# Class: ESCB 


_Concept representing region Cantabria in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CB](https://w3id.org/lmodel/dpv/loc/ES-CB)





```mermaid
 classDiagram
    class ESCB
    click ESCB href "../ESCB/"
      ES <|-- ESCB
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CB](https://w3id.org/lmodel/dpv/loc/ES-CB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CB
* Cantabria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CB |
| native | loc:ESCB |
| exact | dpv_loc:ES-CB, dpv_loc_owl:ES-CB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Cantabria in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CB
- Cantabria
exact_mappings:
- dpv_loc:ES-CB
- dpv_loc_owl:ES-CB
is_a: ES
class_uri: loc:ES-CB

```
</details>

### Induced

<details>
```yaml
name: ESCB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Cantabria in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CB
- Cantabria
exact_mappings:
- dpv_loc:ES-CB
- dpv_loc_owl:ES-CB
is_a: ES
class_uri: loc:ES-CB

```
</details></div>