---
search:
  boost: 10.0
---

# Class: NILE 


_Concept representing region León Department in country Nicaragua_



<div data-search-exclude markdown="1">



URI: [loc:NI-LE](https://w3id.org/lmodel/dpv/loc/NI-LE)





```mermaid
 classDiagram
    class NILE
    click NILE href "../NILE/"
      NI <|-- NILE
        click NI href "../NI/"
      
      
```





## Inheritance
* [NI](NI.md)
    * **NILE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NI-LE](https://w3id.org/lmodel/dpv/loc/NI-LE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NI-LE
* León Department




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NI-LE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NI-LE |
| native | loc:NILE |
| exact | dpv_loc:NI-LE, dpv_loc_owl:NI-LE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NILE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NI-LE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region León Department in country Nicaragua
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NI-LE
- León Department
exact_mappings:
- dpv_loc:NI-LE
- dpv_loc_owl:NI-LE
is_a: NI
class_uri: loc:NI-LE

```
</details>

### Induced

<details>
```yaml
name: NILE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NI-LE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region León Department in country Nicaragua
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NI-LE
- León Department
exact_mappings:
- dpv_loc:NI-LE
- dpv_loc_owl:NI-LE
is_a: NI
class_uri: loc:NI-LE

```
</details></div>