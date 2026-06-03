---
search:
  boost: 10.0
---

# Class: BRMG 


_Concept representing region Minas Gerais in country Brazil_



<div data-search-exclude markdown="1">



URI: [loc:BR-MG](https://w3id.org/lmodel/dpv/loc/BR-MG)





```mermaid
 classDiagram
    class BRMG
    click BRMG href "../BRMG/"
      BR <|-- BRMG
        click BR href "../BR/"
      
      
```





## Inheritance
* [BR](BR.md)
    * **BRMG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BR-MG](https://w3id.org/lmodel/dpv/loc/BR-MG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BR-MG
* Minas Gerais




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BR-MG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BR-MG |
| native | loc:BRMG |
| exact | dpv_loc:BR-MG, dpv_loc_owl:BR-MG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BRMG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-MG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Minas Gerais in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-MG
- Minas Gerais
exact_mappings:
- dpv_loc:BR-MG
- dpv_loc_owl:BR-MG
is_a: BR
class_uri: loc:BR-MG

```
</details>

### Induced

<details>
```yaml
name: BRMG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-MG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Minas Gerais in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-MG
- Minas Gerais
exact_mappings:
- dpv_loc:BR-MG
- dpv_loc_owl:BR-MG
is_a: BR
class_uri: loc:BR-MG

```
</details></div>