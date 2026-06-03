---
search:
  boost: 10.0
---

# Class: USMD 


_Concept representing region Maryland in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-MD](https://w3id.org/lmodel/dpv/loc/US-MD)





```mermaid
 classDiagram
    class USMD
    click USMD href "../USMD/"
      US <|-- USMD
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USMD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-MD](https://w3id.org/lmodel/dpv/loc/US-MD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-MD
* Maryland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-MD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-MD |
| native | loc:USMD |
| exact | dpv_loc:US-MD, dpv_loc_owl:US-MD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USMD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Maryland in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MD
- Maryland
exact_mappings:
- dpv_loc:US-MD
- dpv_loc_owl:US-MD
is_a: US
class_uri: loc:US-MD

```
</details>

### Induced

<details>
```yaml
name: USMD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Maryland in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MD
- Maryland
exact_mappings:
- dpv_loc:US-MD
- dpv_loc_owl:US-MD
is_a: US
class_uri: loc:US-MD

```
</details></div>