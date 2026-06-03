---
search:
  boost: 10.0
---

# Class: ESCA 


_Concept representing region Province of Cádiz in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CA](https://w3id.org/lmodel/dpv/loc/ES-CA)





```mermaid
 classDiagram
    class ESCA
    click ESCA href "../ESCA/"
      ES <|-- ESCA
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CA](https://w3id.org/lmodel/dpv/loc/ES-CA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CA
* Province of Cádiz




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CA |
| native | loc:ESCA |
| exact | dpv_loc:ES-CA, dpv_loc_owl:ES-CA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cádiz in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CA
- Province of Cádiz
exact_mappings:
- dpv_loc:ES-CA
- dpv_loc_owl:ES-CA
is_a: ES
class_uri: loc:ES-CA

```
</details>

### Induced

<details>
```yaml
name: ESCA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cádiz in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CA
- Province of Cádiz
exact_mappings:
- dpv_loc:ES-CA
- dpv_loc_owl:ES-CA
is_a: ES
class_uri: loc:ES-CA

```
</details></div>