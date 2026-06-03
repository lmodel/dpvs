---
search:
  boost: 10.0
---

# Class: GBWIL 


_Concept representing region Wiltshire in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-WIL](https://w3id.org/lmodel/dpv/loc/GB-WIL)





```mermaid
 classDiagram
    class GBWIL
    click GBWIL href "../GBWIL/"
      GB <|-- GBWIL
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBWIL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-WIL](https://w3id.org/lmodel/dpv/loc/GB-WIL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-WIL
* Wiltshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-WIL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-WIL |
| native | loc:GBWIL |
| exact | dpv_loc:GB-WIL, dpv_loc_owl:GB-WIL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBWIL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WIL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Wiltshire in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WIL
- Wiltshire
exact_mappings:
- dpv_loc:GB-WIL
- dpv_loc_owl:GB-WIL
is_a: GB
class_uri: loc:GB-WIL

```
</details>

### Induced

<details>
```yaml
name: GBWIL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WIL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Wiltshire in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WIL
- Wiltshire
exact_mappings:
- dpv_loc:GB-WIL
- dpv_loc_owl:GB-WIL
is_a: GB
class_uri: loc:GB-WIL

```
</details></div>