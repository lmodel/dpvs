---
search:
  boost: 10.0
---

# Class: USNM 


_Concept representing region New Mexico in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-NM](https://w3id.org/lmodel/dpv/loc/US-NM)





```mermaid
 classDiagram
    class USNM
    click USNM href "../USNM/"
      US <|-- USNM
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USNM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-NM](https://w3id.org/lmodel/dpv/loc/US-NM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-NM
* New Mexico




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-NM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-NM |
| native | loc:USNM |
| exact | dpv_loc:US-NM, dpv_loc_owl:US-NM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USNM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region New Mexico in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NM
- New Mexico
exact_mappings:
- dpv_loc:US-NM
- dpv_loc_owl:US-NM
is_a: US
class_uri: loc:US-NM

```
</details>

### Induced

<details>
```yaml
name: USNM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region New Mexico in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NM
- New Mexico
exact_mappings:
- dpv_loc:US-NM
- dpv_loc_owl:US-NM
is_a: US
class_uri: loc:US-NM

```
</details></div>