---
search:
  boost: 10.0
---

# Class: ESLE 


_Concept representing region Province of León in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-LE](https://w3id.org/lmodel/dpv/loc/ES-LE)





```mermaid
 classDiagram
    class ESLE
    click ESLE href "../ESLE/"
      ES <|-- ESLE
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESLE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-LE](https://w3id.org/lmodel/dpv/loc/ES-LE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-LE
* Province of León




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-LE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-LE |
| native | loc:ESLE |
| exact | dpv_loc:ES-LE, dpv_loc_owl:ES-LE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESLE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-LE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of León in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-LE
- Province of León
exact_mappings:
- dpv_loc:ES-LE
- dpv_loc_owl:ES-LE
is_a: ES
class_uri: loc:ES-LE

```
</details>

### Induced

<details>
```yaml
name: ESLE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-LE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of León in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-LE
- Province of León
exact_mappings:
- dpv_loc:ES-LE
- dpv_loc_owl:ES-LE
is_a: ES
class_uri: loc:ES-LE

```
</details></div>