---
search:
  boost: 10.0
---

# Class: USUT 


_Concept representing region Utah in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-UT](https://w3id.org/lmodel/dpv/loc/US-UT)





```mermaid
 classDiagram
    class USUT
    click USUT href "../USUT/"
      US <|-- USUT
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USUT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-UT](https://w3id.org/lmodel/dpv/loc/US-UT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-UT
* Utah




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-UT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-UT |
| native | loc:USUT |
| exact | dpv_loc:US-UT, dpv_loc_owl:US-UT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USUT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-UT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Utah in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-UT
- Utah
exact_mappings:
- dpv_loc:US-UT
- dpv_loc_owl:US-UT
is_a: US
class_uri: loc:US-UT

```
</details>

### Induced

<details>
```yaml
name: USUT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-UT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Utah in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-UT
- Utah
exact_mappings:
- dpv_loc:US-UT
- dpv_loc_owl:US-UT
is_a: US
class_uri: loc:US-UT

```
</details></div>