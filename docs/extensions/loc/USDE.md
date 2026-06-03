---
search:
  boost: 10.0
---

# Class: USDE 


_Concept representing region Delaware in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-DE](https://w3id.org/lmodel/dpv/loc/US-DE)





```mermaid
 classDiagram
    class USDE
    click USDE href "../USDE/"
      US <|-- USDE
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USDE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-DE](https://w3id.org/lmodel/dpv/loc/US-DE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-DE
* Delaware




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-DE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-DE |
| native | loc:USDE |
| exact | dpv_loc:US-DE, dpv_loc_owl:US-DE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USDE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-DE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Delaware in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-DE
- Delaware
exact_mappings:
- dpv_loc:US-DE
- dpv_loc_owl:US-DE
is_a: US
class_uri: loc:US-DE

```
</details>

### Induced

<details>
```yaml
name: USDE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-DE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Delaware in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-DE
- Delaware
exact_mappings:
- dpv_loc:US-DE
- dpv_loc_owl:US-DE
is_a: US
class_uri: loc:US-DE

```
</details></div>