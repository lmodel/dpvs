---
search:
  boost: 10.0
---

# Class: USTN 


_Concept representing region Tennessee in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-TN](https://w3id.org/lmodel/dpv/loc/US-TN)





```mermaid
 classDiagram
    class USTN
    click USTN href "../USTN/"
      US <|-- USTN
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USTN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-TN](https://w3id.org/lmodel/dpv/loc/US-TN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-TN
* Tennessee




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-TN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-TN |
| native | loc:USTN |
| exact | dpv_loc:US-TN, dpv_loc_owl:US-TN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USTN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-TN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Tennessee in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-TN
- Tennessee
exact_mappings:
- dpv_loc:US-TN
- dpv_loc_owl:US-TN
is_a: US
class_uri: loc:US-TN

```
</details>

### Induced

<details>
```yaml
name: USTN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-TN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Tennessee in country United States of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-TN
- Tennessee
exact_mappings:
- dpv_loc:US-TN
- dpv_loc_owl:US-TN
is_a: US
class_uri: loc:US-TN

```
</details></div>