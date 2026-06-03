---
search:
  boost: 10.0
---

# Class: USLA 


_Concept representing region Louisiana in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-LA](https://w3id.org/lmodel/dpv/loc/US-LA)





```mermaid
 classDiagram
    class USLA
    click USLA href "../USLA/"
      US <|-- USLA
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USLA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-LA](https://w3id.org/lmodel/dpv/loc/US-LA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-LA
* Louisiana




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-LA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-LA |
| native | loc:USLA |
| exact | dpv_loc:US-LA, dpv_loc_owl:US-LA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USLA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-LA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Louisiana in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-LA
- Louisiana
exact_mappings:
- dpv_loc:US-LA
- dpv_loc_owl:US-LA
is_a: US
class_uri: loc:US-LA

```
</details>

### Induced

<details>
```yaml
name: USLA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-LA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Louisiana in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-LA
- Louisiana
exact_mappings:
- dpv_loc:US-LA
- dpv_loc_owl:US-LA
is_a: US
class_uri: loc:US-LA

```
</details></div>