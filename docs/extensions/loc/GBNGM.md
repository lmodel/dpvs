---
search:
  boost: 10.0
---

# Class: GBNGM 


_Concept representing region Nottingham in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-NGM](https://w3id.org/lmodel/dpv/loc/GB-NGM)





```mermaid
 classDiagram
    class GBNGM
    click GBNGM href "../GBNGM/"
      GB <|-- GBNGM
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBNGM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-NGM](https://w3id.org/lmodel/dpv/loc/GB-NGM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-NGM
* Nottingham




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-NGM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-NGM |
| native | loc:GBNGM |
| exact | dpv_loc:GB-NGM, dpv_loc_owl:GB-NGM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBNGM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NGM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Nottingham in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NGM
- Nottingham
exact_mappings:
- dpv_loc:GB-NGM
- dpv_loc_owl:GB-NGM
is_a: GB
class_uri: loc:GB-NGM

```
</details>

### Induced

<details>
```yaml
name: GBNGM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NGM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Nottingham in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NGM
- Nottingham
exact_mappings:
- dpv_loc:GB-NGM
- dpv_loc_owl:GB-NGM
is_a: GB
class_uri: loc:GB-NGM

```
</details></div>