---
search:
  boost: 10.0
---

# Class: USIA 


_Concept representing region Iowa in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-IA](https://w3id.org/lmodel/dpv/loc/US-IA)





```mermaid
 classDiagram
    class USIA
    click USIA href "../USIA/"
      US <|-- USIA
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USIA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-IA](https://w3id.org/lmodel/dpv/loc/US-IA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-IA
* Iowa




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-IA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-IA |
| native | loc:USIA |
| exact | dpv_loc:US-IA, dpv_loc_owl:US-IA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USIA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-IA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Iowa in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-IA
- Iowa
exact_mappings:
- dpv_loc:US-IA
- dpv_loc_owl:US-IA
is_a: US
class_uri: loc:US-IA

```
</details>

### Induced

<details>
```yaml
name: USIA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-IA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Iowa in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-IA
- Iowa
exact_mappings:
- dpv_loc:US-IA
- dpv_loc_owl:US-IA
is_a: US
class_uri: loc:US-IA

```
</details></div>