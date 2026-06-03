---
search:
  boost: 10.0
---

# Class: USIN 


_Concept representing region Indiana in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-IN](https://w3id.org/lmodel/dpv/loc/US-IN)





```mermaid
 classDiagram
    class USIN
    click USIN href "../USIN/"
      US <|-- USIN
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USIN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-IN](https://w3id.org/lmodel/dpv/loc/US-IN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-IN
* Indiana




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-IN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-IN |
| native | loc:USIN |
| exact | dpv_loc:US-IN, dpv_loc_owl:US-IN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USIN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-IN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Indiana in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-IN
- Indiana
exact_mappings:
- dpv_loc:US-IN
- dpv_loc_owl:US-IN
is_a: US
class_uri: loc:US-IN

```
</details>

### Induced

<details>
```yaml
name: USIN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-IN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Indiana in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-IN
- Indiana
exact_mappings:
- dpv_loc:US-IN
- dpv_loc_owl:US-IN
is_a: US
class_uri: loc:US-IN

```
</details></div>