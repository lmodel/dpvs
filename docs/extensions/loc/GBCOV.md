---
search:
  boost: 10.0
---

# Class: GBCOV 


_Concept representing region City of Coventry in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-COV](https://w3id.org/lmodel/dpv/loc/GB-COV)





```mermaid
 classDiagram
    class GBCOV
    click GBCOV href "../GBCOV/"
      GB <|-- GBCOV
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBCOV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-COV](https://w3id.org/lmodel/dpv/loc/GB-COV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-COV
* City of Coventry




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-COV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-COV |
| native | loc:GBCOV |
| exact | dpv_loc:GB-COV, dpv_loc_owl:GB-COV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBCOV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-COV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Coventry in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-COV
- City of Coventry
exact_mappings:
- dpv_loc:GB-COV
- dpv_loc_owl:GB-COV
is_a: GB
class_uri: loc:GB-COV

```
</details>

### Induced

<details>
```yaml
name: GBCOV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-COV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Coventry in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-COV
- City of Coventry
exact_mappings:
- dpv_loc:GB-COV
- dpv_loc_owl:GB-COV
is_a: GB
class_uri: loc:GB-COV

```
</details></div>