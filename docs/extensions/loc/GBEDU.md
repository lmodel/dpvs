---
search:
  boost: 10.0
---

# Class: GBEDU 


_Concept representing region East Dunbartonshire in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-EDU](https://w3id.org/lmodel/dpv/loc/GB-EDU)





```mermaid
 classDiagram
    class GBEDU
    click GBEDU href "../GBEDU/"
      GB <|-- GBEDU
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBEDU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-EDU](https://w3id.org/lmodel/dpv/loc/GB-EDU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-EDU
* East Dunbartonshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-EDU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-EDU |
| native | loc:GBEDU |
| exact | dpv_loc:GB-EDU, dpv_loc_owl:GB-EDU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBEDU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-EDU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region East Dunbartonshire in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-EDU
- East Dunbartonshire
exact_mappings:
- dpv_loc:GB-EDU
- dpv_loc_owl:GB-EDU
is_a: GB
class_uri: loc:GB-EDU

```
</details>

### Induced

<details>
```yaml
name: GBEDU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-EDU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region East Dunbartonshire in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-EDU
- East Dunbartonshire
exact_mappings:
- dpv_loc:GB-EDU
- dpv_loc_owl:GB-EDU
is_a: GB
class_uri: loc:GB-EDU

```
</details></div>