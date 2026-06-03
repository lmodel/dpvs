---
search:
  boost: 10.0
---

# Class: USNJ 


_Concept representing region New Jersey in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-NJ](https://w3id.org/lmodel/dpv/loc/US-NJ)





```mermaid
 classDiagram
    class USNJ
    click USNJ href "../USNJ/"
      US <|-- USNJ
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USNJ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-NJ](https://w3id.org/lmodel/dpv/loc/US-NJ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-NJ
* New Jersey




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-NJ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-NJ |
| native | loc:USNJ |
| exact | dpv_loc:US-NJ, dpv_loc_owl:US-NJ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USNJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region New Jersey in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NJ
- New Jersey
exact_mappings:
- dpv_loc:US-NJ
- dpv_loc_owl:US-NJ
is_a: US
class_uri: loc:US-NJ

```
</details>

### Induced

<details>
```yaml
name: USNJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region New Jersey in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NJ
- New Jersey
exact_mappings:
- dpv_loc:US-NJ
- dpv_loc_owl:US-NJ
is_a: US
class_uri: loc:US-NJ

```
</details></div>