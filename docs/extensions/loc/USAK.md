---
search:
  boost: 10.0
---

# Class: USAK 


_Concept representing region Alaska in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-AK](https://w3id.org/lmodel/dpv/loc/US-AK)





```mermaid
 classDiagram
    class USAK
    click USAK href "../USAK/"
      US <|-- USAK
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USAK**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-AK](https://w3id.org/lmodel/dpv/loc/US-AK) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-AK
* Alaska




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-AK |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-AK |
| native | loc:USAK |
| exact | dpv_loc:US-AK, dpv_loc_owl:US-AK |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USAK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Alaska in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AK
- Alaska
exact_mappings:
- dpv_loc:US-AK
- dpv_loc_owl:US-AK
is_a: US
class_uri: loc:US-AK

```
</details>

### Induced

<details>
```yaml
name: USAK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Alaska in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AK
- Alaska
exact_mappings:
- dpv_loc:US-AK
- dpv_loc_owl:US-AK
is_a: US
class_uri: loc:US-AK

```
</details></div>