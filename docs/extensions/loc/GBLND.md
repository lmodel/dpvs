---
search:
  boost: 10.0
---

# Class: GBLND 


_Concept representing region City of London in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-LND](https://w3id.org/lmodel/dpv/loc/GB-LND)





```mermaid
 classDiagram
    class GBLND
    click GBLND href "../GBLND/"
      GB <|-- GBLND
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBLND**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-LND](https://w3id.org/lmodel/dpv/loc/GB-LND) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-LND
* City of London




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-LND |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-LND |
| native | loc:GBLND |
| exact | dpv_loc:GB-LND, dpv_loc_owl:GB-LND |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBLND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of London in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LND
- City of London
exact_mappings:
- dpv_loc:GB-LND
- dpv_loc_owl:GB-LND
is_a: GB
class_uri: loc:GB-LND

```
</details>

### Induced

<details>
```yaml
name: GBLND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of London in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LND
- City of London
exact_mappings:
- dpv_loc:GB-LND
- dpv_loc_owl:GB-LND
is_a: GB
class_uri: loc:GB-LND

```
</details></div>