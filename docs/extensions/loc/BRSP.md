---
search:
  boost: 10.0
---

# Class: BRSP 


_Concept representing region São Paulo (state) in country Brazil_



<div data-search-exclude markdown="1">



URI: [loc:BR-SP](https://w3id.org/lmodel/dpv/loc/BR-SP)





```mermaid
 classDiagram
    class BRSP
    click BRSP href "../BRSP/"
      BR <|-- BRSP
        click BR href "../BR/"
      
      
```





## Inheritance
* [BR](BR.md)
    * **BRSP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BR-SP](https://w3id.org/lmodel/dpv/loc/BR-SP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BR-SP
* São Paulo (state)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BR-SP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BR-SP |
| native | loc:BRSP |
| exact | dpv_loc:BR-SP, dpv_loc_owl:BR-SP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BRSP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-SP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region São Paulo (state) in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-SP
- São Paulo (state)
exact_mappings:
- dpv_loc:BR-SP
- dpv_loc_owl:BR-SP
is_a: BR
class_uri: loc:BR-SP

```
</details>

### Induced

<details>
```yaml
name: BRSP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-SP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region São Paulo (state) in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-SP
- São Paulo (state)
exact_mappings:
- dpv_loc:BR-SP
- dpv_loc_owl:BR-SP
is_a: BR
class_uri: loc:BR-SP

```
</details></div>