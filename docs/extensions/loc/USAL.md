---
search:
  boost: 10.0
---

# Class: USAL 


_Concept representing region Alabama in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-AL](https://w3id.org/lmodel/dpv/loc/US-AL)





```mermaid
 classDiagram
    class USAL
    click USAL href "../USAL/"
      US <|-- USAL
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USAL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-AL](https://w3id.org/lmodel/dpv/loc/US-AL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-AL
* Alabama




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-AL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-AL |
| native | loc:USAL |
| exact | dpv_loc:US-AL, dpv_loc_owl:US-AL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Alabama in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AL
- Alabama
exact_mappings:
- dpv_loc:US-AL
- dpv_loc_owl:US-AL
is_a: US
class_uri: loc:US-AL

```
</details>

### Induced

<details>
```yaml
name: USAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Alabama in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AL
- Alabama
exact_mappings:
- dpv_loc:US-AL
- dpv_loc_owl:US-AL
is_a: US
class_uri: loc:US-AL

```
</details></div>