---
search:
  boost: 10.0
---

# Class: ESSS 


_Concept representing region Gipuzkoa in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-SS](https://w3id.org/lmodel/dpv/loc/ES-SS)





```mermaid
 classDiagram
    class ESSS
    click ESSS href "../ESSS/"
      ES <|-- ESSS
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESSS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-SS](https://w3id.org/lmodel/dpv/loc/ES-SS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-SS
* Gipuzkoa




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-SS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-SS |
| native | loc:ESSS |
| exact | dpv_loc:ES-SS, dpv_loc_owl:ES-SS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESSS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gipuzkoa in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SS
- Gipuzkoa
exact_mappings:
- dpv_loc:ES-SS
- dpv_loc_owl:ES-SS
is_a: ES
class_uri: loc:ES-SS

```
</details>

### Induced

<details>
```yaml
name: ESSS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gipuzkoa in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SS
- Gipuzkoa
exact_mappings:
- dpv_loc:ES-SS
- dpv_loc_owl:ES-SS
is_a: ES
class_uri: loc:ES-SS

```
</details></div>