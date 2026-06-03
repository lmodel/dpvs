---
search:
  boost: 10.0
---

# Class: ESGI 


_Concept representing region Province of Girona in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-GI](https://w3id.org/lmodel/dpv/loc/ES-GI)





```mermaid
 classDiagram
    class ESGI
    click ESGI href "../ESGI/"
      ES <|-- ESGI
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESGI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-GI](https://w3id.org/lmodel/dpv/loc/ES-GI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-GI
* Province of Girona




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-GI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-GI |
| native | loc:ESGI |
| exact | dpv_loc:ES-GI, dpv_loc_owl:ES-GI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESGI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-GI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Girona in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-GI
- Province of Girona
exact_mappings:
- dpv_loc:ES-GI
- dpv_loc_owl:ES-GI
is_a: ES
class_uri: loc:ES-GI

```
</details>

### Induced

<details>
```yaml
name: ESGI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-GI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Girona in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-GI
- Province of Girona
exact_mappings:
- dpv_loc:ES-GI
- dpv_loc_owl:ES-GI
is_a: ES
class_uri: loc:ES-GI

```
</details></div>