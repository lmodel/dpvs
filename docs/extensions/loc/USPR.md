---
search:
  boost: 10.0
---

# Class: USPR 


_Concept representing region Puerto Rico in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-PR](https://w3id.org/lmodel/dpv/loc/US-PR)





```mermaid
 classDiagram
    class USPR
    click USPR href "../USPR/"
      US <|-- USPR
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USPR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-PR](https://w3id.org/lmodel/dpv/loc/US-PR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-PR
* Puerto Rico




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-PR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-PR |
| native | loc:USPR |
| exact | dpv_loc:US-PR, dpv_loc_owl:US-PR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USPR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-PR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Puerto Rico in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-PR
- Puerto Rico
exact_mappings:
- dpv_loc:US-PR
- dpv_loc_owl:US-PR
is_a: US
class_uri: loc:US-PR

```
</details>

### Induced

<details>
```yaml
name: USPR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-PR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Puerto Rico in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-PR
- Puerto Rico
exact_mappings:
- dpv_loc:US-PR
- dpv_loc_owl:US-PR
is_a: US
class_uri: loc:US-PR

```
</details></div>