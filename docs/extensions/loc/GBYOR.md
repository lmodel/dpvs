---
search:
  boost: 10.0
---

# Class: GBYOR 


_Concept representing region City of York in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-YOR](https://w3id.org/lmodel/dpv/loc/GB-YOR)





```mermaid
 classDiagram
    class GBYOR
    click GBYOR href "../GBYOR/"
      GB <|-- GBYOR
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBYOR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-YOR](https://w3id.org/lmodel/dpv/loc/GB-YOR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-YOR
* City of York




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-YOR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-YOR |
| native | loc:GBYOR |
| exact | dpv_loc:GB-YOR, dpv_loc_owl:GB-YOR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBYOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-YOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of York in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-YOR
- City of York
exact_mappings:
- dpv_loc:GB-YOR
- dpv_loc_owl:GB-YOR
is_a: GB
class_uri: loc:GB-YOR

```
</details>

### Induced

<details>
```yaml
name: GBYOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-YOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of York in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-YOR
- City of York
exact_mappings:
- dpv_loc:GB-YOR
- dpv_loc_owl:GB-YOR
is_a: GB
class_uri: loc:GB-YOR

```
</details></div>