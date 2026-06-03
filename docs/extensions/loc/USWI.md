---
search:
  boost: 10.0
---

# Class: USWI 


_Concept representing region Wisconsin in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-WI](https://w3id.org/lmodel/dpv/loc/US-WI)





```mermaid
 classDiagram
    class USWI
    click USWI href "../USWI/"
      US <|-- USWI
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USWI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-WI](https://w3id.org/lmodel/dpv/loc/US-WI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-WI
* Wisconsin




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-WI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-WI |
| native | loc:USWI |
| exact | dpv_loc:US-WI, dpv_loc_owl:US-WI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USWI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-WI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Wisconsin in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-WI
- Wisconsin
exact_mappings:
- dpv_loc:US-WI
- dpv_loc_owl:US-WI
is_a: US
class_uri: loc:US-WI

```
</details>

### Induced

<details>
```yaml
name: USWI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-WI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Wisconsin in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-WI
- Wisconsin
exact_mappings:
- dpv_loc:US-WI
- dpv_loc_owl:US-WI
is_a: US
class_uri: loc:US-WI

```
</details></div>