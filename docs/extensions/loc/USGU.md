---
search:
  boost: 10.0
---

# Class: USGU 


_Concept representing region Guam in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-GU](https://w3id.org/lmodel/dpv/loc/US-GU)





```mermaid
 classDiagram
    class USGU
    click USGU href "../USGU/"
      US <|-- USGU
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USGU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-GU](https://w3id.org/lmodel/dpv/loc/US-GU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-GU
* Guam




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-GU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-GU |
| native | loc:USGU |
| exact | dpv_loc:US-GU, dpv_loc_owl:US-GU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USGU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-GU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Guam in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-GU
- Guam
exact_mappings:
- dpv_loc:US-GU
- dpv_loc_owl:US-GU
is_a: US
class_uri: loc:US-GU

```
</details>

### Induced

<details>
```yaml
name: USGU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-GU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Guam in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-GU
- Guam
exact_mappings:
- dpv_loc:US-GU
- dpv_loc_owl:US-GU
is_a: US
class_uri: loc:US-GU

```
</details></div>