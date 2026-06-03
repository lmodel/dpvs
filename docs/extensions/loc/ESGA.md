---
search:
  boost: 10.0
---

# Class: ESGA 


_Concept representing region Galicia (Spain) in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-GA](https://w3id.org/lmodel/dpv/loc/ES-GA)





```mermaid
 classDiagram
    class ESGA
    click ESGA href "../ESGA/"
      ES <|-- ESGA
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESGA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-GA](https://w3id.org/lmodel/dpv/loc/ES-GA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-GA
* Galicia (Spain)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-GA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-GA |
| native | loc:ESGA |
| exact | dpv_loc:ES-GA, dpv_loc_owl:ES-GA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESGA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-GA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Galicia (Spain) in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-GA
- Galicia (Spain)
exact_mappings:
- dpv_loc:ES-GA
- dpv_loc_owl:ES-GA
is_a: ES
class_uri: loc:ES-GA

```
</details>

### Induced

<details>
```yaml
name: ESGA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-GA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Galicia (Spain) in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-GA
- Galicia (Spain)
exact_mappings:
- dpv_loc:ES-GA
- dpv_loc_owl:ES-GA
is_a: ES
class_uri: loc:ES-GA

```
</details></div>