---
search:
  boost: 10.0
---

# Class: USID 


_Concept representing region Idaho in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-ID](https://w3id.org/lmodel/dpv/loc/US-ID)





```mermaid
 classDiagram
    class USID
    click USID href "../USID/"
      US <|-- USID
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USID**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-ID](https://w3id.org/lmodel/dpv/loc/US-ID) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-ID
* Idaho




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-ID |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-ID |
| native | loc:USID |
| exact | dpv_loc:US-ID, dpv_loc_owl:US-ID |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-ID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Idaho in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-ID
- Idaho
exact_mappings:
- dpv_loc:US-ID
- dpv_loc_owl:US-ID
is_a: US
class_uri: loc:US-ID

```
</details>

### Induced

<details>
```yaml
name: USID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-ID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Idaho in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-ID
- Idaho
exact_mappings:
- dpv_loc:US-ID
- dpv_loc_owl:US-ID
is_a: US
class_uri: loc:US-ID

```
</details></div>