---
search:
  boost: 10.0
---

# Class: USMS 


_Concept representing region Mississippi (state) in country United States_

_of America_



<div data-search-exclude markdown="1">



URI: [loc:US-MS](https://w3id.org/lmodel/dpv/loc/US-MS)





```mermaid
 classDiagram
    class USMS
    click USMS href "../USMS/"
      US <|-- USMS
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USMS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-MS](https://w3id.org/lmodel/dpv/loc/US-MS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-MS
* Mississippi (state)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-MS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-MS |
| native | loc:USMS |
| exact | dpv_loc:US-MS, dpv_loc_owl:US-MS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USMS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Mississippi (state) in country United States

  of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MS
- Mississippi (state)
exact_mappings:
- dpv_loc:US-MS
- dpv_loc_owl:US-MS
is_a: US
class_uri: loc:US-MS

```
</details>

### Induced

<details>
```yaml
name: USMS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Mississippi (state) in country United States

  of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MS
- Mississippi (state)
exact_mappings:
- dpv_loc:US-MS
- dpv_loc_owl:US-MS
is_a: US
class_uri: loc:US-MS

```
</details></div>