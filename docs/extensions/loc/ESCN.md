---
search:
  boost: 10.0
---

# Class: ESCN 


_Concept representing region Canary Islands in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CN](https://w3id.org/lmodel/dpv/loc/ES-CN)





```mermaid
 classDiagram
    class ESCN
    click ESCN href "../ESCN/"
      ES <|-- ESCN
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CN](https://w3id.org/lmodel/dpv/loc/ES-CN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CN
* Canary Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CN |
| native | loc:ESCN |
| exact | dpv_loc:ES-CN, dpv_loc_owl:ES-CN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canary Islands in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CN
- Canary Islands
exact_mappings:
- dpv_loc:ES-CN
- dpv_loc_owl:ES-CN
is_a: ES
class_uri: loc:ES-CN

```
</details>

### Induced

<details>
```yaml
name: ESCN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canary Islands in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CN
- Canary Islands
exact_mappings:
- dpv_loc:ES-CN
- dpv_loc_owl:ES-CN
is_a: ES
class_uri: loc:ES-CN

```
</details></div>