---
search:
  boost: 10.0
---

# Class: GBHAM 


_Concept representing region Hampshire in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-HAM](https://w3id.org/lmodel/dpv/loc/GB-HAM)





```mermaid
 classDiagram
    class GBHAM
    click GBHAM href "../GBHAM/"
      GB <|-- GBHAM
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBHAM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-HAM](https://w3id.org/lmodel/dpv/loc/GB-HAM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-HAM
* Hampshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-HAM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-HAM |
| native | loc:GBHAM |
| exact | dpv_loc:GB-HAM, dpv_loc_owl:GB-HAM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBHAM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-HAM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Hampshire in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-HAM
- Hampshire
exact_mappings:
- dpv_loc:GB-HAM
- dpv_loc_owl:GB-HAM
is_a: GB
class_uri: loc:GB-HAM

```
</details>

### Induced

<details>
```yaml
name: GBHAM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-HAM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Hampshire in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-HAM
- Hampshire
exact_mappings:
- dpv_loc:GB-HAM
- dpv_loc_owl:GB-HAM
is_a: GB
class_uri: loc:GB-HAM

```
</details></div>