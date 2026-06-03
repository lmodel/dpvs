---
search:
  boost: 10.0
---

# Class: USME 


_Concept representing region Maine in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-ME](https://w3id.org/lmodel/dpv/loc/US-ME)





```mermaid
 classDiagram
    class USME
    click USME href "../USME/"
      US <|-- USME
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USME**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-ME](https://w3id.org/lmodel/dpv/loc/US-ME) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-ME
* Maine




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-ME |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-ME |
| native | loc:USME |
| exact | dpv_loc:US-ME, dpv_loc_owl:US-ME |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USME
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-ME
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Maine in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-ME
- Maine
exact_mappings:
- dpv_loc:US-ME
- dpv_loc_owl:US-ME
is_a: US
class_uri: loc:US-ME

```
</details>

### Induced

<details>
```yaml
name: USME
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-ME
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Maine in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-ME
- Maine
exact_mappings:
- dpv_loc:US-ME
- dpv_loc_owl:US-ME
is_a: US
class_uri: loc:US-ME

```
</details></div>