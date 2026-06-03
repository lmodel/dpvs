---
search:
  boost: 10.0
---

# Class: USVA 


_Concept representing region Virginia in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-VA](https://w3id.org/lmodel/dpv/loc/US-VA)





```mermaid
 classDiagram
    class USVA
    click USVA href "../USVA/"
      US <|-- USVA
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USVA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-VA](https://w3id.org/lmodel/dpv/loc/US-VA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-VA
* Virginia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-VA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-VA |
| native | loc:USVA |
| exact | dpv_loc:US-VA, dpv_loc_owl:US-VA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USVA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-VA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Virginia in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-VA
- Virginia
exact_mappings:
- dpv_loc:US-VA
- dpv_loc_owl:US-VA
is_a: US
class_uri: loc:US-VA

```
</details>

### Induced

<details>
```yaml
name: USVA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-VA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Virginia in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-VA
- Virginia
exact_mappings:
- dpv_loc:US-VA
- dpv_loc_owl:US-VA
is_a: US
class_uri: loc:US-VA

```
</details></div>