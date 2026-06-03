---
search:
  boost: 10.0
---

# Class: USMA 


_Concept representing region Massachusetts in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-MA](https://w3id.org/lmodel/dpv/loc/US-MA)





```mermaid
 classDiagram
    class USMA
    click USMA href "../USMA/"
      US <|-- USMA
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USMA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-MA](https://w3id.org/lmodel/dpv/loc/US-MA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-MA
* Massachusetts




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-MA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-MA |
| native | loc:USMA |
| exact | dpv_loc:US-MA, dpv_loc_owl:US-MA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USMA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Massachusetts in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MA
- Massachusetts
exact_mappings:
- dpv_loc:US-MA
- dpv_loc_owl:US-MA
is_a: US
class_uri: loc:US-MA

```
</details>

### Induced

<details>
```yaml
name: USMA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Massachusetts in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MA
- Massachusetts
exact_mappings:
- dpv_loc:US-MA
- dpv_loc_owl:US-MA
is_a: US
class_uri: loc:US-MA

```
</details></div>