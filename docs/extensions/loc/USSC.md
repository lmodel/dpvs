---
search:
  boost: 10.0
---

# Class: USSC 


_Concept representing region South Carolina in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-SC](https://w3id.org/lmodel/dpv/loc/US-SC)





```mermaid
 classDiagram
    class USSC
    click USSC href "../USSC/"
      US <|-- USSC
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USSC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-SC](https://w3id.org/lmodel/dpv/loc/US-SC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-SC
* South Carolina




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-SC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-SC |
| native | loc:USSC |
| exact | dpv_loc:US-SC, dpv_loc_owl:US-SC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USSC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-SC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region South Carolina in country United States
  of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-SC
- South Carolina
exact_mappings:
- dpv_loc:US-SC
- dpv_loc_owl:US-SC
is_a: US
class_uri: loc:US-SC

```
</details>

### Induced

<details>
```yaml
name: USSC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-SC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region South Carolina in country United States
  of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-SC
- South Carolina
exact_mappings:
- dpv_loc:US-SC
- dpv_loc_owl:US-SC
is_a: US
class_uri: loc:US-SC

```
</details></div>