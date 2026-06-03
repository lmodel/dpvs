---
search:
  boost: 10.0
---

# Class: USOR 


_Concept representing region Oregon in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-OR](https://w3id.org/lmodel/dpv/loc/US-OR)





```mermaid
 classDiagram
    class USOR
    click USOR href "../USOR/"
      US <|-- USOR
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USOR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-OR](https://w3id.org/lmodel/dpv/loc/US-OR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-OR
* Oregon




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-OR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-OR |
| native | loc:USOR |
| exact | dpv_loc:US-OR, dpv_loc_owl:US-OR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-OR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Oregon in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-OR
- Oregon
exact_mappings:
- dpv_loc:US-OR
- dpv_loc_owl:US-OR
is_a: US
class_uri: loc:US-OR

```
</details>

### Induced

<details>
```yaml
name: USOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-OR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Oregon in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-OR
- Oregon
exact_mappings:
- dpv_loc:US-OR
- dpv_loc_owl:US-OR
is_a: US
class_uri: loc:US-OR

```
</details></div>