---
search:
  boost: 10.0
---

# Class: ESM 


_Concept representing region Province of Madrid in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-M](https://w3id.org/lmodel/dpv/loc/ES-M)





```mermaid
 classDiagram
    class ESM
    click ESM href "../ESM/"
      ES <|-- ESM
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-M](https://w3id.org/lmodel/dpv/loc/ES-M) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-M
* Province of Madrid




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-M |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-M |
| native | loc:ESM |
| exact | dpv_loc:ES-M, dpv_loc_owl:ES-M |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-M
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Madrid in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-M
- Province of Madrid
exact_mappings:
- dpv_loc:ES-M
- dpv_loc_owl:ES-M
is_a: ES
class_uri: loc:ES-M

```
</details>

### Induced

<details>
```yaml
name: ESM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-M
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Madrid in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-M
- Province of Madrid
exact_mappings:
- dpv_loc:ES-M
- dpv_loc_owl:ES-M
is_a: ES
class_uri: loc:ES-M

```
</details></div>