---
search:
  boost: 10.0
---

# Class: USHI 


_Concept representing region Hawaii in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-HI](https://w3id.org/lmodel/dpv/loc/US-HI)





```mermaid
 classDiagram
    class USHI
    click USHI href "../USHI/"
      US <|-- USHI
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USHI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-HI](https://w3id.org/lmodel/dpv/loc/US-HI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-HI
* Hawaii




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-HI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-HI |
| native | loc:USHI |
| exact | dpv_loc:US-HI, dpv_loc_owl:US-HI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USHI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-HI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hawaii in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-HI
- Hawaii
exact_mappings:
- dpv_loc:US-HI
- dpv_loc_owl:US-HI
is_a: US
class_uri: loc:US-HI

```
</details>

### Induced

<details>
```yaml
name: USHI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-HI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hawaii in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-HI
- Hawaii
exact_mappings:
- dpv_loc:US-HI
- dpv_loc_owl:US-HI
is_a: US
class_uri: loc:US-HI

```
</details></div>