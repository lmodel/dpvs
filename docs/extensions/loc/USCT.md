---
search:
  boost: 10.0
---

# Class: USCT 


_Concept representing region Connecticut in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-CT](https://w3id.org/lmodel/dpv/loc/US-CT)





```mermaid
 classDiagram
    class USCT
    click USCT href "../USCT/"
      US <|-- USCT
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USCT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-CT](https://w3id.org/lmodel/dpv/loc/US-CT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-CT
* Connecticut




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-CT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-CT |
| native | loc:USCT |
| exact | dpv_loc:US-CT, dpv_loc_owl:US-CT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USCT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-CT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Connecticut in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-CT
- Connecticut
exact_mappings:
- dpv_loc:US-CT
- dpv_loc_owl:US-CT
is_a: US
class_uri: loc:US-CT

```
</details>

### Induced

<details>
```yaml
name: USCT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-CT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Connecticut in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-CT
- Connecticut
exact_mappings:
- dpv_loc:US-CT
- dpv_loc_owl:US-CT
is_a: US
class_uri: loc:US-CT

```
</details></div>