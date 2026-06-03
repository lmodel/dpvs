---
search:
  boost: 10.0
---

# Class: GBANS 


_Concept representing region Angus in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ANS](https://w3id.org/lmodel/dpv/loc/GB-ANS)





```mermaid
 classDiagram
    class GBANS
    click GBANS href "../GBANS/"
      GB <|-- GBANS
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBANS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ANS](https://w3id.org/lmodel/dpv/loc/GB-ANS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ANS
* Angus




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ANS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ANS |
| native | loc:GBANS |
| exact | dpv_loc:GB-ANS, dpv_loc_owl:GB-ANS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBANS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ANS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Angus in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ANS
- Angus
exact_mappings:
- dpv_loc:GB-ANS
- dpv_loc_owl:GB-ANS
is_a: GB
class_uri: loc:GB-ANS

```
</details>

### Induced

<details>
```yaml
name: GBANS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ANS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Angus in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ANS
- Angus
exact_mappings:
- dpv_loc:GB-ANS
- dpv_loc_owl:GB-ANS
is_a: GB
class_uri: loc:GB-ANS

```
</details></div>