---
search:
  boost: 10.0
---

# Class: GBELN 


_Concept representing region East Lothian in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ELN](https://w3id.org/lmodel/dpv/loc/GB-ELN)





```mermaid
 classDiagram
    class GBELN
    click GBELN href "../GBELN/"
      GB <|-- GBELN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBELN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ELN](https://w3id.org/lmodel/dpv/loc/GB-ELN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ELN
* East Lothian




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ELN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ELN |
| native | loc:GBELN |
| exact | dpv_loc:GB-ELN, dpv_loc_owl:GB-ELN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBELN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ELN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region East Lothian in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ELN
- East Lothian
exact_mappings:
- dpv_loc:GB-ELN
- dpv_loc_owl:GB-ELN
is_a: GB
class_uri: loc:GB-ELN

```
</details>

### Induced

<details>
```yaml
name: GBELN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ELN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region East Lothian in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ELN
- East Lothian
exact_mappings:
- dpv_loc:GB-ELN
- dpv_loc_owl:GB-ELN
is_a: GB
class_uri: loc:GB-ELN

```
</details></div>