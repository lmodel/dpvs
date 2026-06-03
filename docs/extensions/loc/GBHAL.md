---
search:
  boost: 10.0
---

# Class: GBHAL 


_Concept representing region Borough of Halton in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-HAL](https://w3id.org/lmodel/dpv/loc/GB-HAL)





```mermaid
 classDiagram
    class GBHAL
    click GBHAL href "../GBHAL/"
      GB <|-- GBHAL
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBHAL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-HAL](https://w3id.org/lmodel/dpv/loc/GB-HAL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-HAL
* Borough of Halton




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-HAL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-HAL |
| native | loc:GBHAL |
| exact | dpv_loc:GB-HAL, dpv_loc_owl:GB-HAL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBHAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-HAL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Halton in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-HAL
- Borough of Halton
exact_mappings:
- dpv_loc:GB-HAL
- dpv_loc_owl:GB-HAL
is_a: GB
class_uri: loc:GB-HAL

```
</details>

### Induced

<details>
```yaml
name: GBHAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-HAL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Halton in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-HAL
- Borough of Halton
exact_mappings:
- dpv_loc:GB-HAL
- dpv_loc_owl:GB-HAL
is_a: GB
class_uri: loc:GB-HAL

```
</details></div>