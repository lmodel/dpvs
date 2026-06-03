---
search:
  boost: 10.0
---

# Class: EGMN 


_Concept representing region Minya Governorate in country Egypt_



<div data-search-exclude markdown="1">



URI: [loc:EG-MN](https://w3id.org/lmodel/dpv/loc/EG-MN)





```mermaid
 classDiagram
    class EGMN
    click EGMN href "../EGMN/"
      EG <|-- EGMN
        click EG href "../EG/"
      
      
```





## Inheritance
* [EG](EG.md)
    * **EGMN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:EG-MN](https://w3id.org/lmodel/dpv/loc/EG-MN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* EG-MN
* Minya Governorate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#EG-MN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:EG-MN |
| native | loc:EGMN |
| exact | dpv_loc:EG-MN, dpv_loc_owl:EG-MN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EGMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-MN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Minya Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-MN
- Minya Governorate
exact_mappings:
- dpv_loc:EG-MN
- dpv_loc_owl:EG-MN
is_a: EG
class_uri: loc:EG-MN

```
</details>

### Induced

<details>
```yaml
name: EGMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-MN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Minya Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-MN
- Minya Governorate
exact_mappings:
- dpv_loc:EG-MN
- dpv_loc_owl:EG-MN
is_a: EG
class_uri: loc:EG-MN

```
</details></div>