---
search:
  boost: 10.0
---

# Class: GBNIR 


_Concept representing region Northern Ireland in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-NIR](https://w3id.org/lmodel/dpv/loc/GB-NIR)





```mermaid
 classDiagram
    class GBNIR
    click GBNIR href "../GBNIR/"
      GB <|-- GBNIR
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBNIR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-NIR](https://w3id.org/lmodel/dpv/loc/GB-NIR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-NIR
* Northern Ireland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-NIR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-NIR |
| native | loc:GBNIR |
| exact | dpv_loc:GB-NIR, dpv_loc_owl:GB-NIR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBNIR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NIR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Northern Ireland in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NIR
- Northern Ireland
exact_mappings:
- dpv_loc:GB-NIR
- dpv_loc_owl:GB-NIR
is_a: GB
class_uri: loc:GB-NIR

```
</details>

### Induced

<details>
```yaml
name: GBNIR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NIR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Northern Ireland in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NIR
- Northern Ireland
exact_mappings:
- dpv_loc:GB-NIR
- dpv_loc_owl:GB-NIR
is_a: GB
class_uri: loc:GB-NIR

```
</details></div>