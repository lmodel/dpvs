---
search:
  boost: 10.0
---

# Class: USAS 


_Concept representing region American Samoa in country United States of_

_America_



<div data-search-exclude markdown="1">



URI: [loc:US-AS](https://w3id.org/lmodel/dpv/loc/US-AS)





```mermaid
 classDiagram
    class USAS
    click USAS href "../USAS/"
      US <|-- USAS
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USAS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-AS](https://w3id.org/lmodel/dpv/loc/US-AS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-AS
* American Samoa




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-AS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-AS |
| native | loc:USAS |
| exact | dpv_loc:US-AS, dpv_loc_owl:US-AS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USAS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region American Samoa in country United States
  of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AS
- American Samoa
exact_mappings:
- dpv_loc:US-AS
- dpv_loc_owl:US-AS
is_a: US
class_uri: loc:US-AS

```
</details>

### Induced

<details>
```yaml
name: USAS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-AS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region American Samoa in country United States
  of

  America'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-AS
- American Samoa
exact_mappings:
- dpv_loc:US-AS
- dpv_loc_owl:US-AS
is_a: US
class_uri: loc:US-AS

```
</details></div>