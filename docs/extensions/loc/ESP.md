---
search:
  boost: 10.0
---

# Class: ESP 


_Concept representing region Province of Palencia in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-P](https://w3id.org/lmodel/dpv/loc/ES-P)





```mermaid
 classDiagram
    class ESP
    click ESP href "../ESP/"
      ES <|-- ESP
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-P](https://w3id.org/lmodel/dpv/loc/ES-P) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-P
* Province of Palencia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-P |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-P |
| native | loc:ESP |
| exact | dpv_loc:ES-P, dpv_loc_owl:ES-P |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-P
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Palencia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-P
- Province of Palencia
exact_mappings:
- dpv_loc:ES-P
- dpv_loc_owl:ES-P
is_a: ES
class_uri: loc:ES-P

```
</details>

### Induced

<details>
```yaml
name: ESP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-P
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Palencia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-P
- Province of Palencia
exact_mappings:
- dpv_loc:ES-P
- dpv_loc_owl:ES-P
is_a: ES
class_uri: loc:ES-P

```
</details></div>