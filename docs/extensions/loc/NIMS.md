---
search:
  boost: 10.0
---

# Class: NIMS 


_Concept representing region Masaya Department in country Nicaragua_



<div data-search-exclude markdown="1">



URI: [loc:NI-MS](https://w3id.org/lmodel/dpv/loc/NI-MS)





```mermaid
 classDiagram
    class NIMS
    click NIMS href "../NIMS/"
      NI <|-- NIMS
        click NI href "../NI/"
      
      
```





## Inheritance
* [NI](NI.md)
    * **NIMS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NI-MS](https://w3id.org/lmodel/dpv/loc/NI-MS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NI-MS
* Masaya Department




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NI-MS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NI-MS |
| native | loc:NIMS |
| exact | dpv_loc:NI-MS, dpv_loc_owl:NI-MS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NIMS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NI-MS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Masaya Department in country Nicaragua
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NI-MS
- Masaya Department
exact_mappings:
- dpv_loc:NI-MS
- dpv_loc_owl:NI-MS
is_a: NI
class_uri: loc:NI-MS

```
</details>

### Induced

<details>
```yaml
name: NIMS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NI-MS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Masaya Department in country Nicaragua
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NI-MS
- Masaya Department
exact_mappings:
- dpv_loc:NI-MS
- dpv_loc_owl:NI-MS
is_a: NI
class_uri: loc:NI-MS

```
</details></div>