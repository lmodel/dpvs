---
search:
  boost: 10.0
---

# Class: USGA 


_Concept representing region Georgia (U.S. state) in country United_

_States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-GA](https://w3id.org/lmodel/dpv/loc/US-GA)





```mermaid
 classDiagram
    class USGA
    click USGA href "../USGA/"
      US <|-- USGA
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USGA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-GA](https://w3id.org/lmodel/dpv/loc/US-GA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-GA
* Georgia (U.S. state)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-GA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-GA |
| native | loc:USGA |
| exact | dpv_loc:US-GA, dpv_loc_owl:US-GA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USGA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-GA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Georgia (U.S. state) in country United

  States of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-GA
- Georgia (U.S. state)
exact_mappings:
- dpv_loc:US-GA
- dpv_loc_owl:US-GA
is_a: US
class_uri: loc:US-GA

```
</details>

### Induced

<details>
```yaml
name: USGA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-GA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Georgia (U.S. state) in country United

  States of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-GA
- Georgia (U.S. state)
exact_mappings:
- dpv_loc:US-GA
- dpv_loc_owl:US-GA
is_a: US
class_uri: loc:US-GA

```
</details></div>