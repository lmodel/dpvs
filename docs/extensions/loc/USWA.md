---
search:
  boost: 10.0
---

# Class: USWA 


_Concept representing region Washington (state) in country United States_

_of America_



<div data-search-exclude markdown="1">



URI: [loc:US-WA](https://w3id.org/lmodel/dpv/loc/US-WA)





```mermaid
 classDiagram
    class USWA
    click USWA href "../USWA/"
      US <|-- USWA
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USWA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-WA](https://w3id.org/lmodel/dpv/loc/US-WA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-WA
* Washington (state)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-WA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-WA |
| native | loc:USWA |
| exact | dpv_loc:US-WA, dpv_loc_owl:US-WA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USWA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-WA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Washington (state) in country United States

  of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-WA
- Washington (state)
exact_mappings:
- dpv_loc:US-WA
- dpv_loc_owl:US-WA
is_a: US
class_uri: loc:US-WA

```
</details>

### Induced

<details>
```yaml
name: USWA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-WA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Washington (state) in country United States

  of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-WA
- Washington (state)
exact_mappings:
- dpv_loc:US-WA
- dpv_loc_owl:US-WA
is_a: US
class_uri: loc:US-WA

```
</details></div>