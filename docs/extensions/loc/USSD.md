---
search:
  boost: 10.0
---

# Class: USSD 


_Concept representing region South Dakota in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-SD](https://w3id.org/lmodel/dpv/loc/US-SD)





```mermaid
 classDiagram
    class USSD
    click USSD href "../USSD/"
      US <|-- USSD
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USSD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-SD](https://w3id.org/lmodel/dpv/loc/US-SD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-SD
* South Dakota




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-SD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-SD |
| native | loc:USSD |
| exact | dpv_loc:US-SD, dpv_loc_owl:US-SD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USSD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-SD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region South Dakota in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-SD
- South Dakota
exact_mappings:
- dpv_loc:US-SD
- dpv_loc_owl:US-SD
is_a: US
class_uri: loc:US-SD

```
</details>

### Induced

<details>
```yaml
name: USSD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-SD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region South Dakota in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-SD
- South Dakota
exact_mappings:
- dpv_loc:US-SD
- dpv_loc_owl:US-SD
is_a: US
class_uri: loc:US-SD

```
</details></div>