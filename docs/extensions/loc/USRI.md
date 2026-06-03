---
search:
  boost: 10.0
---

# Class: USRI 


_Concept representing region Rhode Island in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-RI](https://w3id.org/lmodel/dpv/loc/US-RI)





```mermaid
 classDiagram
    class USRI
    click USRI href "../USRI/"
      US <|-- USRI
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USRI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-RI](https://w3id.org/lmodel/dpv/loc/US-RI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-RI
* Rhode Island




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-RI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-RI |
| native | loc:USRI |
| exact | dpv_loc:US-RI, dpv_loc_owl:US-RI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USRI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-RI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Rhode Island in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-RI
- Rhode Island
exact_mappings:
- dpv_loc:US-RI
- dpv_loc_owl:US-RI
is_a: US
class_uri: loc:US-RI

```
</details>

### Induced

<details>
```yaml
name: USRI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-RI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Rhode Island in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-RI
- Rhode Island
exact_mappings:
- dpv_loc:US-RI
- dpv_loc_owl:US-RI
is_a: US
class_uri: loc:US-RI

```
</details></div>