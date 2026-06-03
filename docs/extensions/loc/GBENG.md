---
search:
  boost: 10.0
---

# Class: GBENG 


_Concept representing region England in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ENG](https://w3id.org/lmodel/dpv/loc/GB-ENG)





```mermaid
 classDiagram
    class GBENG
    click GBENG href "../GBENG/"
      GB <|-- GBENG
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBENG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ENG](https://w3id.org/lmodel/dpv/loc/GB-ENG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ENG
* England




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ENG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ENG |
| native | loc:GBENG |
| exact | dpv_loc:GB-ENG, dpv_loc_owl:GB-ENG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBENG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ENG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region England in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ENG
- England
exact_mappings:
- dpv_loc:GB-ENG
- dpv_loc_owl:GB-ENG
is_a: GB
class_uri: loc:GB-ENG

```
</details>

### Induced

<details>
```yaml
name: GBENG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ENG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region England in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ENG
- England
exact_mappings:
- dpv_loc:GB-ENG
- dpv_loc_owl:GB-ENG
is_a: GB
class_uri: loc:GB-ENG

```
</details></div>