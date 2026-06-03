---
search:
  boost: 10.0
---

# Class: GBCMN 


_Concept representing region Carmarthenshire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-CMN](https://w3id.org/lmodel/dpv/loc/GB-CMN)





```mermaid
 classDiagram
    class GBCMN
    click GBCMN href "../GBCMN/"
      GB <|-- GBCMN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBCMN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-CMN](https://w3id.org/lmodel/dpv/loc/GB-CMN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-CMN
* Carmarthenshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-CMN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-CMN |
| native | loc:GBCMN |
| exact | dpv_loc:GB-CMN, dpv_loc_owl:GB-CMN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBCMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-CMN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Carmarthenshire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-CMN
- Carmarthenshire
exact_mappings:
- dpv_loc:GB-CMN
- dpv_loc_owl:GB-CMN
is_a: GB
class_uri: loc:GB-CMN

```
</details>

### Induced

<details>
```yaml
name: GBCMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-CMN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Carmarthenshire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-CMN
- Carmarthenshire
exact_mappings:
- dpv_loc:GB-CMN
- dpv_loc_owl:GB-CMN
is_a: GB
class_uri: loc:GB-CMN

```
</details></div>