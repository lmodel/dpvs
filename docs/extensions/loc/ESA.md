---
search:
  boost: 10.0
---

# Class: ESA 


_Concept representing region Province of Alicante in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-A](https://w3id.org/lmodel/dpv/loc/ES-A)





```mermaid
 classDiagram
    class ESA
    click ESA href "../ESA/"
      ES <|-- ESA
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-A](https://w3id.org/lmodel/dpv/loc/ES-A) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-A
* Province of Alicante




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-A |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-A |
| native | loc:ESA |
| exact | dpv_loc:ES-A, dpv_loc_owl:ES-A |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-A
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Alicante in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-A
- Province of Alicante
exact_mappings:
- dpv_loc:ES-A
- dpv_loc_owl:ES-A
is_a: ES
class_uri: loc:ES-A

```
</details>

### Induced

<details>
```yaml
name: ESA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-A
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Alicante in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-A
- Province of Alicante
exact_mappings:
- dpv_loc:ES-A
- dpv_loc_owl:ES-A
is_a: ES
class_uri: loc:ES-A

```
</details></div>