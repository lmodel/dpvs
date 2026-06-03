---
search:
  boost: 10.0
---

# Class: GBSTH 


_Concept representing region Southampton in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-STH](https://w3id.org/lmodel/dpv/loc/GB-STH)





```mermaid
 classDiagram
    class GBSTH
    click GBSTH href "../GBSTH/"
      GB <|-- GBSTH
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSTH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-STH](https://w3id.org/lmodel/dpv/loc/GB-STH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-STH
* Southampton




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-STH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-STH |
| native | loc:GBSTH |
| exact | dpv_loc:GB-STH, dpv_loc_owl:GB-STH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSTH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-STH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Southampton in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-STH
- Southampton
exact_mappings:
- dpv_loc:GB-STH
- dpv_loc_owl:GB-STH
is_a: GB
class_uri: loc:GB-STH

```
</details>

### Induced

<details>
```yaml
name: GBSTH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-STH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Southampton in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-STH
- Southampton
exact_mappings:
- dpv_loc:GB-STH
- dpv_loc_owl:GB-STH
is_a: GB
class_uri: loc:GB-STH

```
</details></div>