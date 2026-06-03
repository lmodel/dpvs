---
search:
  boost: 10.0
---

# Class: GBWAR 


_Concept representing region Warwickshire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-WAR](https://w3id.org/lmodel/dpv/loc/GB-WAR)





```mermaid
 classDiagram
    class GBWAR
    click GBWAR href "../GBWAR/"
      GB <|-- GBWAR
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBWAR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-WAR](https://w3id.org/lmodel/dpv/loc/GB-WAR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-WAR
* Warwickshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-WAR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-WAR |
| native | loc:GBWAR |
| exact | dpv_loc:GB-WAR, dpv_loc_owl:GB-WAR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBWAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WAR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Warwickshire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WAR
- Warwickshire
exact_mappings:
- dpv_loc:GB-WAR
- dpv_loc_owl:GB-WAR
is_a: GB
class_uri: loc:GB-WAR

```
</details>

### Induced

<details>
```yaml
name: GBWAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WAR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Warwickshire in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WAR
- Warwickshire
exact_mappings:
- dpv_loc:GB-WAR
- dpv_loc_owl:GB-WAR
is_a: GB
class_uri: loc:GB-WAR

```
</details></div>