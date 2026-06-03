---
search:
  boost: 10.0
---

# Class: BRRJ 


_Concept representing region Rio de Janeiro (state) in country Brazil_



<div data-search-exclude markdown="1">



URI: [loc:BR-RJ](https://w3id.org/lmodel/dpv/loc/BR-RJ)





```mermaid
 classDiagram
    class BRRJ
    click BRRJ href "../BRRJ/"
      BR <|-- BRRJ
        click BR href "../BR/"
      
      
```





## Inheritance
* [BR](BR.md)
    * **BRRJ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BR-RJ](https://w3id.org/lmodel/dpv/loc/BR-RJ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BR-RJ
* Rio de Janeiro (state)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BR-RJ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BR-RJ |
| native | loc:BRRJ |
| exact | dpv_loc:BR-RJ, dpv_loc_owl:BR-RJ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BRRJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-RJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Rio de Janeiro (state) in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-RJ
- Rio de Janeiro (state)
exact_mappings:
- dpv_loc:BR-RJ
- dpv_loc_owl:BR-RJ
is_a: BR
class_uri: loc:BR-RJ

```
</details>

### Induced

<details>
```yaml
name: BRRJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-RJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Rio de Janeiro (state) in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-RJ
- Rio de Janeiro (state)
exact_mappings:
- dpv_loc:BR-RJ
- dpv_loc_owl:BR-RJ
is_a: BR
class_uri: loc:BR-RJ

```
</details></div>