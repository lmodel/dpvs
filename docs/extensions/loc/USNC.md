---
search:
  boost: 10.0
---

# Class: USNC 


_Concept representing region North Carolina in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-NC](https://w3id.org/lmodel/dpv/loc/US-NC)





```mermaid
 classDiagram
    class USNC
    click USNC href "../USNC/"
      US <|-- USNC
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USNC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-NC](https://w3id.org/lmodel/dpv/loc/US-NC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-NC
* North Carolina




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-NC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-NC |
| native | loc:USNC |
| exact | dpv_loc:US-NC, dpv_loc_owl:US-NC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USNC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region North Carolina in country United States
  of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NC
- North Carolina
exact_mappings:
- dpv_loc:US-NC
- dpv_loc_owl:US-NC
is_a: US
class_uri: loc:US-NC

```
</details>

### Induced

<details>
```yaml
name: USNC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region North Carolina in country United States
  of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NC
- North Carolina
exact_mappings:
- dpv_loc:US-NC
- dpv_loc_owl:US-NC
is_a: US
class_uri: loc:US-NC

```
</details></div>