---
search:
  boost: 10.0
---

# Class: ESZ 


_Concept representing region Province of Zaragoza in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-Z](https://w3id.org/lmodel/dpv/loc/ES-Z)





```mermaid
 classDiagram
    class ESZ
    click ESZ href "../ESZ/"
      ES <|-- ESZ
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESZ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-Z](https://w3id.org/lmodel/dpv/loc/ES-Z) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-Z
* Province of Zaragoza




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-Z |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-Z |
| native | loc:ESZ |
| exact | dpv_loc:ES-Z, dpv_loc_owl:ES-Z |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-Z
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Zaragoza in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-Z
- Province of Zaragoza
exact_mappings:
- dpv_loc:ES-Z
- dpv_loc_owl:ES-Z
is_a: ES
class_uri: loc:ES-Z

```
</details>

### Induced

<details>
```yaml
name: ESZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-Z
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Zaragoza in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-Z
- Province of Zaragoza
exact_mappings:
- dpv_loc:ES-Z
- dpv_loc_owl:ES-Z
is_a: ES
class_uri: loc:ES-Z

```
</details></div>