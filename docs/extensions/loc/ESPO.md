---
search:
  boost: 10.0
---

# Class: ESPO 


_Concept representing region Province of Pontevedra in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-PO](https://w3id.org/lmodel/dpv/loc/ES-PO)





```mermaid
 classDiagram
    class ESPO
    click ESPO href "../ESPO/"
      ES <|-- ESPO
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESPO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-PO](https://w3id.org/lmodel/dpv/loc/ES-PO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-PO
* Province of Pontevedra




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-PO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-PO |
| native | loc:ESPO |
| exact | dpv_loc:ES-PO, dpv_loc_owl:ES-PO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESPO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-PO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pontevedra in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-PO
- Province of Pontevedra
exact_mappings:
- dpv_loc:ES-PO
- dpv_loc_owl:ES-PO
is_a: ES
class_uri: loc:ES-PO

```
</details>

### Induced

<details>
```yaml
name: ESPO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-PO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pontevedra in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-PO
- Province of Pontevedra
exact_mappings:
- dpv_loc:ES-PO
- dpv_loc_owl:ES-PO
is_a: ES
class_uri: loc:ES-PO

```
</details></div>