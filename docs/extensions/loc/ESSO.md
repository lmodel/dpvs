---
search:
  boost: 10.0
---

# Class: ESSO 


_Concept representing region Province of Soria in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-SO](https://w3id.org/lmodel/dpv/loc/ES-SO)





```mermaid
 classDiagram
    class ESSO
    click ESSO href "../ESSO/"
      ES <|-- ESSO
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESSO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-SO](https://w3id.org/lmodel/dpv/loc/ES-SO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-SO
* Province of Soria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-SO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-SO |
| native | loc:ESSO |
| exact | dpv_loc:ES-SO, dpv_loc_owl:ES-SO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESSO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Soria in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SO
- Province of Soria
exact_mappings:
- dpv_loc:ES-SO
- dpv_loc_owl:ES-SO
is_a: ES
class_uri: loc:ES-SO

```
</details>

### Induced

<details>
```yaml
name: ESSO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Soria in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SO
- Province of Soria
exact_mappings:
- dpv_loc:ES-SO
- dpv_loc_owl:ES-SO
is_a: ES
class_uri: loc:ES-SO

```
</details></div>