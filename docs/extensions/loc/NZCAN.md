---
search:
  boost: 10.0
---

# Class: NZCAN 


_Concept representing region Canterbury Region in country New Zealand_



<div data-search-exclude markdown="1">



URI: [loc:NZ-CAN](https://w3id.org/lmodel/dpv/loc/NZ-CAN)





```mermaid
 classDiagram
    class NZCAN
    click NZCAN href "../NZCAN/"
      NZ <|-- NZCAN
        click NZ href "../NZ/"
      
      
```





## Inheritance
* [NZ](NZ.md)
    * **NZCAN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NZ-CAN](https://w3id.org/lmodel/dpv/loc/NZ-CAN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NZ-CAN
* Canterbury Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NZ-CAN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NZ-CAN |
| native | loc:NZCAN |
| exact | dpv_loc:NZ-CAN, dpv_loc_owl:NZ-CAN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NZCAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-CAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canterbury Region in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-CAN
- Canterbury Region
exact_mappings:
- dpv_loc:NZ-CAN
- dpv_loc_owl:NZ-CAN
is_a: NZ
class_uri: loc:NZ-CAN

```
</details>

### Induced

<details>
```yaml
name: NZCAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-CAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Canterbury Region in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-CAN
- Canterbury Region
exact_mappings:
- dpv_loc:NZ-CAN
- dpv_loc_owl:NZ-CAN
is_a: NZ
class_uri: loc:NZ-CAN

```
</details></div>