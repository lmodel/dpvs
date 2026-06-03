---
search:
  boost: 10.0
---

# Class: USOH 


_Concept representing region Ohio in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-OH](https://w3id.org/lmodel/dpv/loc/US-OH)





```mermaid
 classDiagram
    class USOH
    click USOH href "../USOH/"
      US <|-- USOH
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USOH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-OH](https://w3id.org/lmodel/dpv/loc/US-OH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-OH
* Ohio




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-OH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-OH |
| native | loc:USOH |
| exact | dpv_loc:US-OH, dpv_loc_owl:US-OH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USOH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-OH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ohio in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-OH
- Ohio
exact_mappings:
- dpv_loc:US-OH
- dpv_loc_owl:US-OH
is_a: US
class_uri: loc:US-OH

```
</details>

### Induced

<details>
```yaml
name: USOH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-OH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ohio in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-OH
- Ohio
exact_mappings:
- dpv_loc:US-OH
- dpv_loc_owl:US-OH
is_a: US
class_uri: loc:US-OH

```
</details></div>