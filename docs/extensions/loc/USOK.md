---
search:
  boost: 10.0
---

# Class: USOK 


_Concept representing region Oklahoma in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-OK](https://w3id.org/lmodel/dpv/loc/US-OK)





```mermaid
 classDiagram
    class USOK
    click USOK href "../USOK/"
      US <|-- USOK
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USOK**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-OK](https://w3id.org/lmodel/dpv/loc/US-OK) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-OK
* Oklahoma




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-OK |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-OK |
| native | loc:USOK |
| exact | dpv_loc:US-OK, dpv_loc_owl:US-OK |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USOK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-OK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Oklahoma in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-OK
- Oklahoma
exact_mappings:
- dpv_loc:US-OK
- dpv_loc_owl:US-OK
is_a: US
class_uri: loc:US-OK

```
</details>

### Induced

<details>
```yaml
name: USOK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-OK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Oklahoma in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-OK
- Oklahoma
exact_mappings:
- dpv_loc:US-OK
- dpv_loc_owl:US-OK
is_a: US
class_uri: loc:US-OK

```
</details></div>