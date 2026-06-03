---
search:
  boost: 10.0
---

# Class: GBDEN 


_Concept representing region Denbighshire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-DEN](https://w3id.org/lmodel/dpv/loc/GB-DEN)





```mermaid
 classDiagram
    class GBDEN
    click GBDEN href "../GBDEN/"
      GB <|-- GBDEN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBDEN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-DEN](https://w3id.org/lmodel/dpv/loc/GB-DEN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-DEN
* Denbighshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-DEN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-DEN |
| native | loc:GBDEN |
| exact | dpv_loc:GB-DEN, dpv_loc_owl:GB-DEN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBDEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DEN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Denbighshire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DEN
- Denbighshire
exact_mappings:
- dpv_loc:GB-DEN
- dpv_loc_owl:GB-DEN
is_a: GB
class_uri: loc:GB-DEN

```
</details>

### Induced

<details>
```yaml
name: GBDEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DEN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Denbighshire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DEN
- Denbighshire
exact_mappings:
- dpv_loc:GB-DEN
- dpv_loc_owl:GB-DEN
is_a: GB
class_uri: loc:GB-DEN

```
</details></div>