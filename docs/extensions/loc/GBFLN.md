---
search:
  boost: 10.0
---

# Class: GBFLN 


_Concept representing region Flintshire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-FLN](https://w3id.org/lmodel/dpv/loc/GB-FLN)





```mermaid
 classDiagram
    class GBFLN
    click GBFLN href "../GBFLN/"
      GB <|-- GBFLN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBFLN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-FLN](https://w3id.org/lmodel/dpv/loc/GB-FLN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-FLN
* Flintshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-FLN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-FLN |
| native | loc:GBFLN |
| exact | dpv_loc:GB-FLN, dpv_loc_owl:GB-FLN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBFLN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-FLN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Flintshire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-FLN
- Flintshire
exact_mappings:
- dpv_loc:GB-FLN
- dpv_loc_owl:GB-FLN
is_a: GB
class_uri: loc:GB-FLN

```
</details>

### Induced

<details>
```yaml
name: GBFLN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-FLN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Flintshire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-FLN
- Flintshire
exact_mappings:
- dpv_loc:GB-FLN
- dpv_loc_owl:GB-FLN
is_a: GB
class_uri: loc:GB-FLN

```
</details></div>