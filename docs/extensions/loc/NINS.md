---
search:
  boost: 10.0
---

# Class: NINS 


_Concept representing region Nueva Segovia Department in country_

_Nicaragua_



<div data-search-exclude markdown="1">



URI: [loc:NI-NS](https://w3id.org/lmodel/dpv/loc/NI-NS)





```mermaid
 classDiagram
    class NINS
    click NINS href "../NINS/"
      NI <|-- NINS
        click NI href "../NI/"
      
      
```





## Inheritance
* [NI](NI.md)
    * **NINS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NI-NS](https://w3id.org/lmodel/dpv/loc/NI-NS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NI-NS
* Nueva Segovia Department




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NI-NS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NI-NS |
| native | loc:NINS |
| exact | dpv_loc:NI-NS, dpv_loc_owl:NI-NS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NINS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NI-NS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Nueva Segovia Department in country

  Nicaragua'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NI-NS
- Nueva Segovia Department
exact_mappings:
- dpv_loc:NI-NS
- dpv_loc_owl:NI-NS
is_a: NI
class_uri: loc:NI-NS

```
</details>

### Induced

<details>
```yaml
name: NINS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NI-NS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Nueva Segovia Department in country

  Nicaragua'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NI-NS
- Nueva Segovia Department
exact_mappings:
- dpv_loc:NI-NS
- dpv_loc_owl:NI-NS
is_a: NI
class_uri: loc:NI-NS

```
</details></div>