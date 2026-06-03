---
search:
  boost: 10.0
---

# Class: GBFIF 


_Concept representing region Fife in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-FIF](https://w3id.org/lmodel/dpv/loc/GB-FIF)





```mermaid
 classDiagram
    class GBFIF
    click GBFIF href "../GBFIF/"
      GB <|-- GBFIF
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBFIF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-FIF](https://w3id.org/lmodel/dpv/loc/GB-FIF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-FIF
* Fife




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-FIF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-FIF |
| native | loc:GBFIF |
| exact | dpv_loc:GB-FIF, dpv_loc_owl:GB-FIF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBFIF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-FIF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Fife in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-FIF
- Fife
exact_mappings:
- dpv_loc:GB-FIF
- dpv_loc_owl:GB-FIF
is_a: GB
class_uri: loc:GB-FIF

```
</details>

### Induced

<details>
```yaml
name: GBFIF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-FIF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Fife in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-FIF
- Fife
exact_mappings:
- dpv_loc:GB-FIF
- dpv_loc_owl:GB-FIF
is_a: GB
class_uri: loc:GB-FIF

```
</details></div>