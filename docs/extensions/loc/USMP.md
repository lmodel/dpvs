---
search:
  boost: 10.0
---

# Class: USMP 


_Concept representing region Northern Mariana Islands in country United_

_States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-MP](https://w3id.org/lmodel/dpv/loc/US-MP)





```mermaid
 classDiagram
    class USMP
    click USMP href "../USMP/"
      US <|-- USMP
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USMP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-MP](https://w3id.org/lmodel/dpv/loc/US-MP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-MP
* Northern Mariana Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-MP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-MP |
| native | loc:USMP |
| exact | dpv_loc:US-MP, dpv_loc_owl:US-MP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USMP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Northern Mariana Islands in country United

  States of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MP
- Northern Mariana Islands
exact_mappings:
- dpv_loc:US-MP
- dpv_loc_owl:US-MP
is_a: US
class_uri: loc:US-MP

```
</details>

### Induced

<details>
```yaml
name: USMP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Northern Mariana Islands in country United

  States of America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MP
- Northern Mariana Islands
exact_mappings:
- dpv_loc:US-MP
- dpv_loc_owl:US-MP
is_a: US
class_uri: loc:US-MP

```
</details></div>