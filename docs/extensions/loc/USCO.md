---
search:
  boost: 10.0
---

# Class: USCO 


_Concept representing region Colorado in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-CO](https://w3id.org/lmodel/dpv/loc/US-CO)





```mermaid
 classDiagram
    class USCO
    click USCO href "../USCO/"
      US <|-- USCO
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USCO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-CO](https://w3id.org/lmodel/dpv/loc/US-CO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-CO
* Colorado




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-CO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-CO |
| native | loc:USCO |
| exact | dpv_loc:US-CO, dpv_loc_owl:US-CO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USCO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-CO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Colorado in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-CO
- Colorado
exact_mappings:
- dpv_loc:US-CO
- dpv_loc_owl:US-CO
is_a: US
class_uri: loc:US-CO

```
</details>

### Induced

<details>
```yaml
name: USCO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-CO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Colorado in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-CO
- Colorado
exact_mappings:
- dpv_loc:US-CO
- dpv_loc_owl:US-CO
is_a: US
class_uri: loc:US-CO

```
</details></div>