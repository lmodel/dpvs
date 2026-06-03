---
search:
  boost: 10.0
---

# Class: ESB 


_Concept representing region Province of Barcelona in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-B](https://w3id.org/lmodel/dpv/loc/ES-B)





```mermaid
 classDiagram
    class ESB
    click ESB href "../ESB/"
      ES <|-- ESB
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-B](https://w3id.org/lmodel/dpv/loc/ES-B) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-B
* Province of Barcelona




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-B |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-B |
| native | loc:ESB |
| exact | dpv_loc:ES-B, dpv_loc_owl:ES-B |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-B
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Barcelona in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-B
- Province of Barcelona
exact_mappings:
- dpv_loc:ES-B
- dpv_loc_owl:ES-B
is_a: ES
class_uri: loc:ES-B

```
</details>

### Induced

<details>
```yaml
name: ESB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-B
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Barcelona in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-B
- Province of Barcelona
exact_mappings:
- dpv_loc:ES-B
- dpv_loc_owl:ES-B
is_a: ES
class_uri: loc:ES-B

```
</details></div>