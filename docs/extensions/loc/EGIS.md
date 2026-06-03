---
search:
  boost: 10.0
---

# Class: EGIS 


_Concept representing region Ismailia Governorate in country Egypt_



<div data-search-exclude markdown="1">



URI: [loc:EG-IS](https://w3id.org/lmodel/dpv/loc/EG-IS)





```mermaid
 classDiagram
    class EGIS
    click EGIS href "../EGIS/"
      EG <|-- EGIS
        click EG href "../EG/"
      
      
```





## Inheritance
* [EG](EG.md)
    * **EGIS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:EG-IS](https://w3id.org/lmodel/dpv/loc/EG-IS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* EG-IS
* Ismailia Governorate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#EG-IS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:EG-IS |
| native | loc:EGIS |
| exact | dpv_loc:EG-IS, dpv_loc_owl:EG-IS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EGIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-IS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ismailia Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-IS
- Ismailia Governorate
exact_mappings:
- dpv_loc:EG-IS
- dpv_loc_owl:EG-IS
is_a: EG
class_uri: loc:EG-IS

```
</details>

### Induced

<details>
```yaml
name: EGIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-IS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ismailia Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-IS
- Ismailia Governorate
exact_mappings:
- dpv_loc:EG-IS
- dpv_loc_owl:EG-IS
is_a: EG
class_uri: loc:EG-IS

```
</details></div>