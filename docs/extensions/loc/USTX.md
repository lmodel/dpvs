---
search:
  boost: 10.0
---

# Class: USTX 


_Concept representing region Texas in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-TX](https://w3id.org/lmodel/dpv/loc/US-TX)





```mermaid
 classDiagram
    class USTX
    click USTX href "../USTX/"
      US <|-- USTX
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USTX**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-TX](https://w3id.org/lmodel/dpv/loc/US-TX) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-TX
* Texas




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-TX |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-TX |
| native | loc:USTX |
| exact | dpv_loc:US-TX, dpv_loc_owl:US-TX |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USTX
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-TX
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Texas in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-TX
- Texas
exact_mappings:
- dpv_loc:US-TX
- dpv_loc_owl:US-TX
is_a: US
class_uri: loc:US-TX

```
</details>

### Induced

<details>
```yaml
name: USTX
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-TX
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Texas in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-TX
- Texas
exact_mappings:
- dpv_loc:US-TX
- dpv_loc_owl:US-TX
is_a: US
class_uri: loc:US-TX

```
</details></div>