---
search:
  boost: 10.0
---

# Class: GBSTT 


_Concept representing region Borough of Stockton-on-Tees in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-STT](https://w3id.org/lmodel/dpv/loc/GB-STT)





```mermaid
 classDiagram
    class GBSTT
    click GBSTT href "../GBSTT/"
      GB <|-- GBSTT
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSTT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-STT](https://w3id.org/lmodel/dpv/loc/GB-STT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-STT
* Borough of Stockton-on-Tees




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-STT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-STT |
| native | loc:GBSTT |
| exact | dpv_loc:GB-STT, dpv_loc_owl:GB-STT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSTT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-STT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Stockton-on-Tees in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-STT
- Borough of Stockton-on-Tees
exact_mappings:
- dpv_loc:GB-STT
- dpv_loc_owl:GB-STT
is_a: GB
class_uri: loc:GB-STT

```
</details>

### Induced

<details>
```yaml
name: GBSTT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-STT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Stockton-on-Tees in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-STT
- Borough of Stockton-on-Tees
exact_mappings:
- dpv_loc:GB-STT
- dpv_loc_owl:GB-STT
is_a: GB
class_uri: loc:GB-STT

```
</details></div>