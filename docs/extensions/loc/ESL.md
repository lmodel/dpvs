---
search:
  boost: 10.0
---

# Class: ESL 


_Concept representing region Province of Lleida in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-L](https://w3id.org/lmodel/dpv/loc/ES-L)





```mermaid
 classDiagram
    class ESL
    click ESL href "../ESL/"
      ES <|-- ESL
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-L](https://w3id.org/lmodel/dpv/loc/ES-L) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-L
* Province of Lleida




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-L |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-L |
| native | loc:ESL |
| exact | dpv_loc:ES-L, dpv_loc_owl:ES-L |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lleida in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-L
- Province of Lleida
exact_mappings:
- dpv_loc:ES-L
- dpv_loc_owl:ES-L
is_a: ES
class_uri: loc:ES-L

```
</details>

### Induced

<details>
```yaml
name: ESL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Lleida in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-L
- Province of Lleida
exact_mappings:
- dpv_loc:ES-L
- dpv_loc_owl:ES-L
is_a: ES
class_uri: loc:ES-L

```
</details></div>