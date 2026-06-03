---
search:
  boost: 10.0
---

# Class: USNE 


_Concept representing region Nebraska in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-NE](https://w3id.org/lmodel/dpv/loc/US-NE)





```mermaid
 classDiagram
    class USNE
    click USNE href "../USNE/"
      US <|-- USNE
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USNE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-NE](https://w3id.org/lmodel/dpv/loc/US-NE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-NE
* Nebraska




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-NE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-NE |
| native | loc:USNE |
| exact | dpv_loc:US-NE, dpv_loc_owl:US-NE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USNE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nebraska in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NE
- Nebraska
exact_mappings:
- dpv_loc:US-NE
- dpv_loc_owl:US-NE
is_a: US
class_uri: loc:US-NE

```
</details>

### Induced

<details>
```yaml
name: USNE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nebraska in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NE
- Nebraska
exact_mappings:
- dpv_loc:US-NE
- dpv_loc_owl:US-NE
is_a: US
class_uri: loc:US-NE

```
</details></div>