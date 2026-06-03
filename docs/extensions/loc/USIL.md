---
search:
  boost: 10.0
---

# Class: USIL 


_Concept representing region Illinois in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-IL](https://w3id.org/lmodel/dpv/loc/US-IL)





```mermaid
 classDiagram
    class USIL
    click USIL href "../USIL/"
      US <|-- USIL
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USIL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-IL](https://w3id.org/lmodel/dpv/loc/US-IL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-IL
* Illinois




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-IL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-IL |
| native | loc:USIL |
| exact | dpv_loc:US-IL, dpv_loc_owl:US-IL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USIL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-IL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Illinois in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-IL
- Illinois
exact_mappings:
- dpv_loc:US-IL
- dpv_loc_owl:US-IL
is_a: US
class_uri: loc:US-IL

```
</details>

### Induced

<details>
```yaml
name: USIL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-IL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Illinois in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-IL
- Illinois
exact_mappings:
- dpv_loc:US-IL
- dpv_loc_owl:US-IL
is_a: US
class_uri: loc:US-IL

```
</details></div>