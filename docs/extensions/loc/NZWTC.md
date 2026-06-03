---
search:
  boost: 10.0
---

# Class: NZWTC 


_Concept representing region West Coast Region in country New Zealand_



<div data-search-exclude markdown="1">



URI: [loc:NZ-WTC](https://w3id.org/lmodel/dpv/loc/NZ-WTC)





```mermaid
 classDiagram
    class NZWTC
    click NZWTC href "../NZWTC/"
      NZ <|-- NZWTC
        click NZ href "../NZ/"
      
      
```





## Inheritance
* [NZ](NZ.md)
    * **NZWTC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NZ-WTC](https://w3id.org/lmodel/dpv/loc/NZ-WTC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NZ-WTC
* West Coast Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NZ-WTC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NZ-WTC |
| native | loc:NZWTC |
| exact | dpv_loc:NZ-WTC, dpv_loc_owl:NZ-WTC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NZWTC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-WTC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region West Coast Region in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-WTC
- West Coast Region
exact_mappings:
- dpv_loc:NZ-WTC
- dpv_loc_owl:NZ-WTC
is_a: NZ
class_uri: loc:NZ-WTC

```
</details>

### Induced

<details>
```yaml
name: NZWTC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-WTC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region West Coast Region in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-WTC
- West Coast Region
exact_mappings:
- dpv_loc:NZ-WTC
- dpv_loc_owl:NZ-WTC
is_a: NZ
class_uri: loc:NZ-WTC

```
</details></div>