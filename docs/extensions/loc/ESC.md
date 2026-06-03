---
search:
  boost: 10.0
---

# Class: ESC 


_Concept representing region Province of A Coruña in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-C](https://w3id.org/lmodel/dpv/loc/ES-C)





```mermaid
 classDiagram
    class ESC
    click ESC href "../ESC/"
      ES <|-- ESC
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-C](https://w3id.org/lmodel/dpv/loc/ES-C) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-C
* Province of A Coruña




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-C |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-C |
| native | loc:ESC |
| exact | dpv_loc:ES-C, dpv_loc_owl:ES-C |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of A Coruña in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-C
- Province of A Coruña
exact_mappings:
- dpv_loc:ES-C
- dpv_loc_owl:ES-C
is_a: ES
class_uri: loc:ES-C

```
</details>

### Induced

<details>
```yaml
name: ESC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of A Coruña in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-C
- Province of A Coruña
exact_mappings:
- dpv_loc:ES-C
- dpv_loc_owl:ES-C
is_a: ES
class_uri: loc:ES-C

```
</details></div>