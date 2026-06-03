---
search:
  boost: 10.0
---

# Class: GBBRD 


_Concept representing region City of Bradford in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-BRD](https://w3id.org/lmodel/dpv/loc/GB-BRD)





```mermaid
 classDiagram
    class GBBRD
    click GBBRD href "../GBBRD/"
      GB <|-- GBBRD
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBBRD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-BRD](https://w3id.org/lmodel/dpv/loc/GB-BRD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-BRD
* City of Bradford




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-BRD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-BRD |
| native | loc:GBBRD |
| exact | dpv_loc:GB-BRD, dpv_loc_owl:GB-BRD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBBRD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BRD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Bradford in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BRD
- City of Bradford
exact_mappings:
- dpv_loc:GB-BRD
- dpv_loc_owl:GB-BRD
is_a: GB
class_uri: loc:GB-BRD

```
</details>

### Induced

<details>
```yaml
name: GBBRD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BRD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Bradford in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BRD
- City of Bradford
exact_mappings:
- dpv_loc:GB-BRD
- dpv_loc_owl:GB-BRD
is_a: GB
class_uri: loc:GB-BRD

```
</details></div>