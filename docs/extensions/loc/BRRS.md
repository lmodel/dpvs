---
search:
  boost: 10.0
---

# Class: BRRS 


_Concept representing region Rio Grande do Sul in country Brazil_



<div data-search-exclude markdown="1">



URI: [loc:BR-RS](https://w3id.org/lmodel/dpv/loc/BR-RS)





```mermaid
 classDiagram
    class BRRS
    click BRRS href "../BRRS/"
      BR <|-- BRRS
        click BR href "../BR/"
      
      
```





## Inheritance
* [BR](BR.md)
    * **BRRS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BR-RS](https://w3id.org/lmodel/dpv/loc/BR-RS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BR-RS
* Rio Grande do Sul




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BR-RS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BR-RS |
| native | loc:BRRS |
| exact | dpv_loc:BR-RS, dpv_loc_owl:BR-RS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BRRS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-RS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Rio Grande do Sul in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-RS
- Rio Grande do Sul
exact_mappings:
- dpv_loc:BR-RS
- dpv_loc_owl:BR-RS
is_a: BR
class_uri: loc:BR-RS

```
</details>

### Induced

<details>
```yaml
name: BRRS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-RS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Rio Grande do Sul in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-RS
- Rio Grande do Sul
exact_mappings:
- dpv_loc:BR-RS
- dpv_loc_owl:BR-RS
is_a: BR
class_uri: loc:BR-RS

```
</details></div>