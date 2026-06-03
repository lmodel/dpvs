---
search:
  boost: 10.0
---

# Class: USVT 


_Concept representing region Vermont in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-VT](https://w3id.org/lmodel/dpv/loc/US-VT)





```mermaid
 classDiagram
    class USVT
    click USVT href "../USVT/"
      US <|-- USVT
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USVT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-VT](https://w3id.org/lmodel/dpv/loc/US-VT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-VT
* Vermont




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-VT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-VT |
| native | loc:USVT |
| exact | dpv_loc:US-VT, dpv_loc_owl:US-VT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USVT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-VT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vermont in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-VT
- Vermont
exact_mappings:
- dpv_loc:US-VT
- dpv_loc_owl:US-VT
is_a: US
class_uri: loc:US-VT

```
</details>

### Induced

<details>
```yaml
name: USVT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-VT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vermont in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-VT
- Vermont
exact_mappings:
- dpv_loc:US-VT
- dpv_loc_owl:US-VT
is_a: US
class_uri: loc:US-VT

```
</details></div>