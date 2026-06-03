---
search:
  boost: 10.0
---

# Class: MAMID 


_Concept representing region Midelt Province in country Morocco_



<div data-search-exclude markdown="1">



URI: [loc:MA-MID](https://w3id.org/lmodel/dpv/loc/MA-MID)





```mermaid
 classDiagram
    class MAMID
    click MAMID href "../MAMID/"
      MA <|-- MAMID
        click MA href "../MA/"
      
      
```





## Inheritance
* [MA](MA.md)
    * **MAMID**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MA-MID](https://w3id.org/lmodel/dpv/loc/MA-MID) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* MA-MID
* Midelt Province




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MA-MID |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MA-MID |
| native | loc:MAMID |
| exact | dpv_loc:MA-MID, dpv_loc_owl:MA-MID |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MAMID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MA-MID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Midelt Province in country Morocco
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MA-MID
- Midelt Province
exact_mappings:
- dpv_loc:MA-MID
- dpv_loc_owl:MA-MID
is_a: MA
class_uri: loc:MA-MID

```
</details>

### Induced

<details>
```yaml
name: MAMID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MA-MID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Midelt Province in country Morocco
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MA-MID
- Midelt Province
exact_mappings:
- dpv_loc:MA-MID
- dpv_loc_owl:MA-MID
is_a: MA
class_uri: loc:MA-MID

```
</details></div>