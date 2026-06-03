---
search:
  boost: 10.0
---

# Class: USCA 


_Concept representing region California in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-CA](https://w3id.org/lmodel/dpv/loc/US-CA)





```mermaid
 classDiagram
    class USCA
    click USCA href "../USCA/"
      US <|-- USCA
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USCA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-CA](https://w3id.org/lmodel/dpv/loc/US-CA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-CA
* California




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-CA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-CA |
| native | loc:USCA |
| exact | dpv_loc:US-CA, dpv_loc_owl:US-CA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USCA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-CA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region California in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-CA
- California
exact_mappings:
- dpv_loc:US-CA
- dpv_loc_owl:US-CA
is_a: US
class_uri: loc:US-CA

```
</details>

### Induced

<details>
```yaml
name: USCA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-CA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region California in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-CA
- California
exact_mappings:
- dpv_loc:US-CA
- dpv_loc_owl:US-CA
is_a: US
class_uri: loc:US-CA

```
</details></div>