---
search:
  boost: 10.0
---

# Class: RSVO 


_Concept representing region Vojvodina in country Serbia_



<div data-search-exclude markdown="1">



URI: [loc:RS-VO](https://w3id.org/lmodel/dpv/loc/RS-VO)





```mermaid
 classDiagram
    class RSVO
    click RSVO href "../RSVO/"
      RS <|-- RSVO
        click RS href "../RS/"
      
      
```





## Inheritance
* [RS](RS.md)
    * **RSVO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RS-VO](https://w3id.org/lmodel/dpv/loc/RS-VO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RS-VO
* Vojvodina




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RS-VO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RS-VO |
| native | loc:RSVO |
| exact | dpv_loc:RS-VO, dpv_loc_owl:RS-VO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RSVO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RS-VO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vojvodina in country Serbia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RS-VO
- Vojvodina
exact_mappings:
- dpv_loc:RS-VO
- dpv_loc_owl:RS-VO
is_a: RS
class_uri: loc:RS-VO

```
</details>

### Induced

<details>
```yaml
name: RSVO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RS-VO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Vojvodina in country Serbia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RS-VO
- Vojvodina
exact_mappings:
- dpv_loc:RS-VO
- dpv_loc_owl:RS-VO
is_a: RS
class_uri: loc:RS-VO

```
</details></div>