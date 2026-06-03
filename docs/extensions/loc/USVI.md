---
search:
  boost: 10.0
---

# Class: USVI 


_Concept representing Region U.S. Virgin Islands in Country USA_



<div data-search-exclude markdown="1">



URI: [loc:US-VI](https://w3id.org/lmodel/dpv/loc/US-VI)





```mermaid
 classDiagram
    class USVI
    click USVI href "../USVI/"
      US <|-- USVI
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USVI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-VI](https://w3id.org/lmodel/dpv/loc/US-VI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-VI
* U.S. Virgin Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-VI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-VI |
| native | loc:USVI |
| exact | dpv_loc:US-VI, dpv_loc_owl:US-VI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USVI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-VI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Region U.S. Virgin Islands in Country USA
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-VI
- U.S. Virgin Islands
exact_mappings:
- dpv_loc:US-VI
- dpv_loc_owl:US-VI
is_a: US
class_uri: loc:US-VI

```
</details>

### Induced

<details>
```yaml
name: USVI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-VI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Region U.S. Virgin Islands in Country USA
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-VI
- U.S. Virgin Islands
exact_mappings:
- dpv_loc:US-VI
- dpv_loc_owl:US-VI
is_a: US
class_uri: loc:US-VI

```
</details></div>