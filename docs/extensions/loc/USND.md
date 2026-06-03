---
search:
  boost: 10.0
---

# Class: USND 


_Concept representing region North Dakota in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-ND](https://w3id.org/lmodel/dpv/loc/US-ND)





```mermaid
 classDiagram
    class USND
    click USND href "../USND/"
      US <|-- USND
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USND**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-ND](https://w3id.org/lmodel/dpv/loc/US-ND) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-ND
* North Dakota




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-ND |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-ND |
| native | loc:USND |
| exact | dpv_loc:US-ND, dpv_loc_owl:US-ND |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-ND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region North Dakota in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-ND
- North Dakota
exact_mappings:
- dpv_loc:US-ND
- dpv_loc_owl:US-ND
is_a: US
class_uri: loc:US-ND

```
</details>

### Induced

<details>
```yaml
name: USND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-ND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region North Dakota in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-ND
- North Dakota
exact_mappings:
- dpv_loc:US-ND
- dpv_loc_owl:US-ND
is_a: US
class_uri: loc:US-ND

```
</details></div>