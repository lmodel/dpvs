---
search:
  boost: 10.0
---

# Class: USWY 


_Concept representing region Wyoming in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-WY](https://w3id.org/lmodel/dpv/loc/US-WY)





```mermaid
 classDiagram
    class USWY
    click USWY href "../USWY/"
      US <|-- USWY
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USWY**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-WY](https://w3id.org/lmodel/dpv/loc/US-WY) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-WY
* Wyoming




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-WY |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-WY |
| native | loc:USWY |
| exact | dpv_loc:US-WY, dpv_loc_owl:US-WY |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USWY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-WY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Wyoming in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-WY
- Wyoming
exact_mappings:
- dpv_loc:US-WY
- dpv_loc_owl:US-WY
is_a: US
class_uri: loc:US-WY

```
</details>

### Induced

<details>
```yaml
name: USWY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-WY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Wyoming in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-WY
- Wyoming
exact_mappings:
- dpv_loc:US-WY
- dpv_loc_owl:US-WY
is_a: US
class_uri: loc:US-WY

```
</details></div>