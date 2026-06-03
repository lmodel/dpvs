---
search:
  boost: 10.0
---

# Class: USNY 


_Concept representing region New York (state) in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-NY](https://w3id.org/lmodel/dpv/loc/US-NY)





```mermaid
 classDiagram
    class USNY
    click USNY href "../USNY/"
      US <|-- USNY
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USNY**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-NY](https://w3id.org/lmodel/dpv/loc/US-NY) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-NY
* New York (state)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-NY |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-NY |
| native | loc:USNY |
| exact | dpv_loc:US-NY, dpv_loc_owl:US-NY |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USNY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region New York (state) in country United States
  of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NY
- New York (state)
exact_mappings:
- dpv_loc:US-NY
- dpv_loc_owl:US-NY
is_a: US
class_uri: loc:US-NY

```
</details>

### Induced

<details>
```yaml
name: USNY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region New York (state) in country United States
  of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NY
- New York (state)
exact_mappings:
- dpv_loc:US-NY
- dpv_loc_owl:US-NY
is_a: US
class_uri: loc:US-NY

```
</details></div>