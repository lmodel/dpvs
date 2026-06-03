---
search:
  boost: 10.0
---

# Class: EGHU 


_Concept representing region Helwan Governorate in country Egypt_



<div data-search-exclude markdown="1">



URI: [loc:EG-HU](https://w3id.org/lmodel/dpv/loc/EG-HU)





```mermaid
 classDiagram
    class EGHU
    click EGHU href "../EGHU/"
      EG <|-- EGHU
        click EG href "../EG/"
      
      
```





## Inheritance
* [EG](EG.md)
    * **EGHU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:EG-HU](https://w3id.org/lmodel/dpv/loc/EG-HU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* EG-HU
* Helwan Governorate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#EG-HU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:EG-HU |
| native | loc:EGHU |
| exact | dpv_loc:EG-HU, dpv_loc_owl:EG-HU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EGHU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-HU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Helwan Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-HU
- Helwan Governorate
exact_mappings:
- dpv_loc:EG-HU
- dpv_loc_owl:EG-HU
is_a: EG
class_uri: loc:EG-HU

```
</details>

### Induced

<details>
```yaml
name: EGHU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-HU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Helwan Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-HU
- Helwan Governorate
exact_mappings:
- dpv_loc:EG-HU
- dpv_loc_owl:EG-HU
is_a: EG
class_uri: loc:EG-HU

```
</details></div>