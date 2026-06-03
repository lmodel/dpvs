---
search:
  boost: 10.0
---

# Class: GBSND 


_Concept representing region City of Sunderland in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-SND](https://w3id.org/lmodel/dpv/loc/GB-SND)





```mermaid
 classDiagram
    class GBSND
    click GBSND href "../GBSND/"
      GB <|-- GBSND
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSND**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-SND](https://w3id.org/lmodel/dpv/loc/GB-SND) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-SND
* City of Sunderland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-SND |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-SND |
| native | loc:GBSND |
| exact | dpv_loc:GB-SND, dpv_loc_owl:GB-SND |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Sunderland in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SND
- City of Sunderland
exact_mappings:
- dpv_loc:GB-SND
- dpv_loc_owl:GB-SND
is_a: GB
class_uri: loc:GB-SND

```
</details>

### Induced

<details>
```yaml
name: GBSND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Sunderland in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SND
- City of Sunderland
exact_mappings:
- dpv_loc:GB-SND
- dpv_loc_owl:GB-SND
is_a: GB
class_uri: loc:GB-SND

```
</details></div>