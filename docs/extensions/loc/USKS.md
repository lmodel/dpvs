---
search:
  boost: 10.0
---

# Class: USKS 


_Concept representing region Kansas in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-KS](https://w3id.org/lmodel/dpv/loc/US-KS)





```mermaid
 classDiagram
    class USKS
    click USKS href "../USKS/"
      US <|-- USKS
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USKS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-KS](https://w3id.org/lmodel/dpv/loc/US-KS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-KS
* Kansas




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-KS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-KS |
| native | loc:USKS |
| exact | dpv_loc:US-KS, dpv_loc_owl:US-KS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USKS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-KS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kansas in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-KS
- Kansas
exact_mappings:
- dpv_loc:US-KS
- dpv_loc_owl:US-KS
is_a: US
class_uri: loc:US-KS

```
</details>

### Induced

<details>
```yaml
name: USKS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-KS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kansas in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-KS
- Kansas
exact_mappings:
- dpv_loc:US-KS
- dpv_loc_owl:US-KS
is_a: US
class_uri: loc:US-KS

```
</details></div>