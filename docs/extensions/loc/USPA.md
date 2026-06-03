---
search:
  boost: 10.0
---

# Class: USPA 


_Concept representing region Pennsylvania in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-PA](https://w3id.org/lmodel/dpv/loc/US-PA)





```mermaid
 classDiagram
    class USPA
    click USPA href "../USPA/"
      US <|-- USPA
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USPA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-PA](https://w3id.org/lmodel/dpv/loc/US-PA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-PA
* Pennsylvania




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-PA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-PA |
| native | loc:USPA |
| exact | dpv_loc:US-PA, dpv_loc_owl:US-PA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USPA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-PA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Pennsylvania in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-PA
- Pennsylvania
exact_mappings:
- dpv_loc:US-PA
- dpv_loc_owl:US-PA
is_a: US
class_uri: loc:US-PA

```
</details>

### Induced

<details>
```yaml
name: USPA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-PA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Pennsylvania in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-PA
- Pennsylvania
exact_mappings:
- dpv_loc:US-PA
- dpv_loc_owl:US-PA
is_a: US
class_uri: loc:US-PA

```
</details></div>