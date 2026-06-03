---
search:
  boost: 10.0
---

# Class: USAR 


_Concept representing region Arkansas in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-AR](https://w3id.org/lmodel/dpv/loc/US-AR)





```mermaid
 classDiagram
    class USAR
    click USAR href "../USAR/"
      US <|-- USAR
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USAR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-AR](https://w3id.org/lmodel/dpv/loc/US-AR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-AR
* Arkansas




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-AR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-AR |
| native | loc:USAR |
| exact | dpv_loc:US-AR, dpv_loc_owl:US-AR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arkansas in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AR
- Arkansas
exact_mappings:
- dpv_loc:US-AR
- dpv_loc_owl:US-AR
is_a: US
class_uri: loc:US-AR

```
</details>

### Induced

<details>
```yaml
name: USAR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arkansas in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AR
- Arkansas
exact_mappings:
- dpv_loc:US-AR
- dpv_loc_owl:US-AR
is_a: US
class_uri: loc:US-AR

```
</details></div>