---
search:
  boost: 10.0
---

# Class: USDC 


_Concept representing region District of Columbia in country United_

_States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-DC](https://w3id.org/lmodel/dpv/loc/US-DC)





```mermaid
 classDiagram
    class USDC
    click USDC href "../USDC/"
      US <|-- USDC
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USDC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-DC](https://w3id.org/lmodel/dpv/loc/US-DC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-DC
* District of Columbia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-DC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-DC |
| native | loc:USDC |
| exact | dpv_loc:US-DC, dpv_loc_owl:US-DC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USDC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-DC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region District of Columbia in country United

  States of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-DC
- District of Columbia
exact_mappings:
- dpv_loc:US-DC
- dpv_loc_owl:US-DC
is_a: US
class_uri: loc:US-DC

```
</details>

### Induced

<details>
```yaml
name: USDC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-DC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region District of Columbia in country United

  States of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-DC
- District of Columbia
exact_mappings:
- dpv_loc:US-DC
- dpv_loc_owl:US-DC
is_a: US
class_uri: loc:US-DC

```
</details></div>