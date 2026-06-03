---
search:
  boost: 10.0
---

# Class: USFL 


_Concept representing region Florida in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-FL](https://w3id.org/lmodel/dpv/loc/US-FL)





```mermaid
 classDiagram
    class USFL
    click USFL href "../USFL/"
      US <|-- USFL
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USFL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-FL](https://w3id.org/lmodel/dpv/loc/US-FL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-FL
* Florida




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-FL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-FL |
| native | loc:USFL |
| exact | dpv_loc:US-FL, dpv_loc_owl:US-FL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USFL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-FL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Florida in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-FL
- Florida
exact_mappings:
- dpv_loc:US-FL
- dpv_loc_owl:US-FL
is_a: US
class_uri: loc:US-FL

```
</details>

### Induced

<details>
```yaml
name: USFL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-FL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Florida in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-FL
- Florida
exact_mappings:
- dpv_loc:US-FL
- dpv_loc_owl:US-FL
is_a: US
class_uri: loc:US-FL

```
</details></div>