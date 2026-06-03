---
search:
  boost: 10.0
---

# Class: USMO 


_Concept representing region Missouri in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-MO](https://w3id.org/lmodel/dpv/loc/US-MO)





```mermaid
 classDiagram
    class USMO
    click USMO href "../USMO/"
      US <|-- USMO
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USMO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-MO](https://w3id.org/lmodel/dpv/loc/US-MO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-MO
* Missouri




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-MO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-MO |
| native | loc:USMO |
| exact | dpv_loc:US-MO, dpv_loc_owl:US-MO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Missouri in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MO
- Missouri
exact_mappings:
- dpv_loc:US-MO
- dpv_loc_owl:US-MO
is_a: US
class_uri: loc:US-MO

```
</details>

### Induced

<details>
```yaml
name: USMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Missouri in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MO
- Missouri
exact_mappings:
- dpv_loc:US-MO
- dpv_loc_owl:US-MO
is_a: US
class_uri: loc:US-MO

```
</details></div>