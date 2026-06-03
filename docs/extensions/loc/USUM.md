---
search:
  boost: 10.0
---

# Class: USUM 


_Concept representing region United States Minor Outlying Islands in_

_country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-UM](https://w3id.org/lmodel/dpv/loc/US-UM)





```mermaid
 classDiagram
    class USUM
    click USUM href "../USUM/"
      US <|-- USUM
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USUM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-UM](https://w3id.org/lmodel/dpv/loc/US-UM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-UM
* United States Minor Outlying Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-UM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-UM |
| native | loc:USUM |
| exact | dpv_loc:US-UM, dpv_loc_owl:US-UM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USUM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-UM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region United States Minor Outlying Islands in

  country United States of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-UM
- United States Minor Outlying Islands
exact_mappings:
- dpv_loc:US-UM
- dpv_loc_owl:US-UM
is_a: US
class_uri: loc:US-UM

```
</details>

### Induced

<details>
```yaml
name: USUM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-UM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region United States Minor Outlying Islands in

  country United States of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-UM
- United States Minor Outlying Islands
exact_mappings:
- dpv_loc:US-UM
- dpv_loc_owl:US-UM
is_a: US
class_uri: loc:US-UM

```
</details></div>