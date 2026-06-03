---
search:
  boost: 10.0
---

# Class: GBLDS 


_Concept representing region City of Leeds in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-LDS](https://w3id.org/lmodel/dpv/loc/GB-LDS)





```mermaid
 classDiagram
    class GBLDS
    click GBLDS href "../GBLDS/"
      GB <|-- GBLDS
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBLDS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-LDS](https://w3id.org/lmodel/dpv/loc/GB-LDS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-LDS
* City of Leeds




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-LDS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-LDS |
| native | loc:GBLDS |
| exact | dpv_loc:GB-LDS, dpv_loc_owl:GB-LDS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBLDS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LDS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Leeds in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LDS
- City of Leeds
exact_mappings:
- dpv_loc:GB-LDS
- dpv_loc_owl:GB-LDS
is_a: GB
class_uri: loc:GB-LDS

```
</details>

### Induced

<details>
```yaml
name: GBLDS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LDS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Leeds in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LDS
- City of Leeds
exact_mappings:
- dpv_loc:GB-LDS
- dpv_loc_owl:GB-LDS
is_a: GB
class_uri: loc:GB-LDS

```
</details></div>