---
search:
  boost: 10.0
---

# Class: USAZ 


_Concept representing region Arizona in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-AZ](https://w3id.org/lmodel/dpv/loc/US-AZ)





```mermaid
 classDiagram
    class USAZ
    click USAZ href "../USAZ/"
      US <|-- USAZ
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USAZ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-AZ](https://w3id.org/lmodel/dpv/loc/US-AZ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-AZ
* Arizona




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-AZ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-AZ |
| native | loc:USAZ |
| exact | dpv_loc:US-AZ, dpv_loc_owl:US-AZ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USAZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AZ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arizona in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AZ
- Arizona
exact_mappings:
- dpv_loc:US-AZ
- dpv_loc_owl:US-AZ
is_a: US
class_uri: loc:US-AZ

```
</details>

### Induced

<details>
```yaml
name: USAZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AZ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arizona in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AZ
- Arizona
exact_mappings:
- dpv_loc:US-AZ
- dpv_loc_owl:US-AZ
is_a: US
class_uri: loc:US-AZ

```
</details></div>