---
search:
  boost: 10.0
---

# Class: GBMEA 


_Concept representing region Mid and East Antrim in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-MEA](https://w3id.org/lmodel/dpv/loc/GB-MEA)





```mermaid
 classDiagram
    class GBMEA
    click GBMEA href "../GBMEA/"
      GB <|-- GBMEA
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBMEA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-MEA](https://w3id.org/lmodel/dpv/loc/GB-MEA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-MEA
* Mid and East Antrim




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-MEA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-MEA |
| native | loc:GBMEA |
| exact | dpv_loc:GB-MEA, dpv_loc_owl:GB-MEA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBMEA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MEA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Mid and East Antrim in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MEA
- Mid and East Antrim
exact_mappings:
- dpv_loc:GB-MEA
- dpv_loc_owl:GB-MEA
is_a: GB
class_uri: loc:GB-MEA

```
</details>

### Induced

<details>
```yaml
name: GBMEA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MEA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Mid and East Antrim in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MEA
- Mid and East Antrim
exact_mappings:
- dpv_loc:GB-MEA
- dpv_loc_owl:GB-MEA
is_a: GB
class_uri: loc:GB-MEA

```
</details></div>