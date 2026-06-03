---
search:
  boost: 10.0
---

# Class: ESSG 


_Concept representing region Province of Segovia in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-SG](https://w3id.org/lmodel/dpv/loc/ES-SG)





```mermaid
 classDiagram
    class ESSG
    click ESSG href "../ESSG/"
      ES <|-- ESSG
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESSG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-SG](https://w3id.org/lmodel/dpv/loc/ES-SG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-SG
* Province of Segovia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-SG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-SG |
| native | loc:ESSG |
| exact | dpv_loc:ES-SG, dpv_loc_owl:ES-SG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESSG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Segovia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SG
- Province of Segovia
exact_mappings:
- dpv_loc:ES-SG
- dpv_loc_owl:ES-SG
is_a: ES
class_uri: loc:ES-SG

```
</details>

### Induced

<details>
```yaml
name: ESSG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Segovia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SG
- Province of Segovia
exact_mappings:
- dpv_loc:ES-SG
- dpv_loc_owl:ES-SG
is_a: ES
class_uri: loc:ES-SG

```
</details></div>