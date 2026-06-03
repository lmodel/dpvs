---
search:
  boost: 10.0
---

# Class: GBMON 


_Concept representing region Monmouthshire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-MON](https://w3id.org/lmodel/dpv/loc/GB-MON)





```mermaid
 classDiagram
    class GBMON
    click GBMON href "../GBMON/"
      GB <|-- GBMON
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBMON**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-MON](https://w3id.org/lmodel/dpv/loc/GB-MON) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-MON
* Monmouthshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-MON |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-MON |
| native | loc:GBMON |
| exact | dpv_loc:GB-MON, dpv_loc_owl:GB-MON |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBMON
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MON
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Monmouthshire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MON
- Monmouthshire
exact_mappings:
- dpv_loc:GB-MON
- dpv_loc_owl:GB-MON
is_a: GB
class_uri: loc:GB-MON

```
</details>

### Induced

<details>
```yaml
name: GBMON
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MON
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Monmouthshire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MON
- Monmouthshire
exact_mappings:
- dpv_loc:GB-MON
- dpv_loc_owl:GB-MON
is_a: GB
class_uri: loc:GB-MON

```
</details></div>