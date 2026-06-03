---
search:
  boost: 10.0
---

# Class: USNH 


_Concept representing region New Hampshire in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-NH](https://w3id.org/lmodel/dpv/loc/US-NH)





```mermaid
 classDiagram
    class USNH
    click USNH href "../USNH/"
      US <|-- USNH
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USNH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-NH](https://w3id.org/lmodel/dpv/loc/US-NH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-NH
* New Hampshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-NH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-NH |
| native | loc:USNH |
| exact | dpv_loc:US-NH, dpv_loc_owl:US-NH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USNH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region New Hampshire in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NH
- New Hampshire
exact_mappings:
- dpv_loc:US-NH
- dpv_loc_owl:US-NH
is_a: US
class_uri: loc:US-NH

```
</details>

### Induced

<details>
```yaml
name: USNH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region New Hampshire in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NH
- New Hampshire
exact_mappings:
- dpv_loc:US-NH
- dpv_loc_owl:US-NH
is_a: US
class_uri: loc:US-NH

```
</details></div>