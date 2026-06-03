---
search:
  boost: 10.0
---

# Class: USMN 


_Concept representing region Minnesota in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-MN](https://w3id.org/lmodel/dpv/loc/US-MN)





```mermaid
 classDiagram
    class USMN
    click USMN href "../USMN/"
      US <|-- USMN
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USMN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-MN](https://w3id.org/lmodel/dpv/loc/US-MN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-MN
* Minnesota




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-MN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-MN |
| native | loc:USMN |
| exact | dpv_loc:US-MN, dpv_loc_owl:US-MN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Minnesota in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MN
- Minnesota
exact_mappings:
- dpv_loc:US-MN
- dpv_loc_owl:US-MN
is_a: US
class_uri: loc:US-MN

```
</details>

### Induced

<details>
```yaml
name: USMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Minnesota in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MN
- Minnesota
exact_mappings:
- dpv_loc:US-MN
- dpv_loc_owl:US-MN
is_a: US
class_uri: loc:US-MN

```
</details></div>