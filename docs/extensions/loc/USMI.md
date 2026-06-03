---
search:
  boost: 10.0
---

# Class: USMI 


_Concept representing region Michigan in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-MI](https://w3id.org/lmodel/dpv/loc/US-MI)





```mermaid
 classDiagram
    class USMI
    click USMI href "../USMI/"
      US <|-- USMI
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USMI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-MI](https://w3id.org/lmodel/dpv/loc/US-MI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-MI
* Michigan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-MI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-MI |
| native | loc:USMI |
| exact | dpv_loc:US-MI, dpv_loc_owl:US-MI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USMI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Michigan in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MI
- Michigan
exact_mappings:
- dpv_loc:US-MI
- dpv_loc_owl:US-MI
is_a: US
class_uri: loc:US-MI

```
</details>

### Induced

<details>
```yaml
name: USMI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Michigan in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MI
- Michigan
exact_mappings:
- dpv_loc:US-MI
- dpv_loc_owl:US-MI
is_a: US
class_uri: loc:US-MI

```
</details></div>