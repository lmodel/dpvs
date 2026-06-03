---
search:
  boost: 10.0
---

# Class: GBLIV 


_Concept representing region Liverpool in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-LIV](https://w3id.org/lmodel/dpv/loc/GB-LIV)





```mermaid
 classDiagram
    class GBLIV
    click GBLIV href "../GBLIV/"
      GB <|-- GBLIV
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBLIV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-LIV](https://w3id.org/lmodel/dpv/loc/GB-LIV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-LIV
* Liverpool




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-LIV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-LIV |
| native | loc:GBLIV |
| exact | dpv_loc:GB-LIV, dpv_loc_owl:GB-LIV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBLIV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LIV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Liverpool in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LIV
- Liverpool
exact_mappings:
- dpv_loc:GB-LIV
- dpv_loc_owl:GB-LIV
is_a: GB
class_uri: loc:GB-LIV

```
</details>

### Induced

<details>
```yaml
name: GBLIV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LIV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Liverpool in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LIV
- Liverpool
exact_mappings:
- dpv_loc:GB-LIV
- dpv_loc_owl:GB-LIV
is_a: GB
class_uri: loc:GB-LIV

```
</details></div>