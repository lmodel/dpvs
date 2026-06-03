---
search:
  boost: 10.0
---

# Class: GBBIR 


_Concept representing region City of Birmingham in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-BIR](https://w3id.org/lmodel/dpv/loc/GB-BIR)





```mermaid
 classDiagram
    class GBBIR
    click GBBIR href "../GBBIR/"
      GB <|-- GBBIR
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBBIR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-BIR](https://w3id.org/lmodel/dpv/loc/GB-BIR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-BIR
* City of Birmingham




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-BIR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-BIR |
| native | loc:GBBIR |
| exact | dpv_loc:GB-BIR, dpv_loc_owl:GB-BIR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBBIR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BIR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Birmingham in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BIR
- City of Birmingham
exact_mappings:
- dpv_loc:GB-BIR
- dpv_loc_owl:GB-BIR
is_a: GB
class_uri: loc:GB-BIR

```
</details>

### Induced

<details>
```yaml
name: GBBIR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BIR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Birmingham in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BIR
- City of Birmingham
exact_mappings:
- dpv_loc:GB-BIR
- dpv_loc_owl:GB-BIR
is_a: GB
class_uri: loc:GB-BIR

```
</details></div>