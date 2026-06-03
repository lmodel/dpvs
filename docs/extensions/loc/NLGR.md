---
search:
  boost: 10.0
---

# Class: NLGR 


_Concept representing region Groningen (province) in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-GR](https://w3id.org/lmodel/dpv/loc/NL-GR)





```mermaid
 classDiagram
    class NLGR
    click NLGR href "../NLGR/"
      NL <|-- NLGR
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLGR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-GR](https://w3id.org/lmodel/dpv/loc/NL-GR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-GR
* Groningen (province)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-GR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-GR |
| native | loc:NLGR |
| exact | dpv_loc:NL-GR, dpv_loc_owl:NL-GR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLGR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-GR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Groningen (province) in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-GR
- Groningen (province)
exact_mappings:
- dpv_loc:NL-GR
- dpv_loc_owl:NL-GR
is_a: NL
class_uri: loc:NL-GR

```
</details>

### Induced

<details>
```yaml
name: NLGR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-GR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Groningen (province) in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-GR
- Groningen (province)
exact_mappings:
- dpv_loc:NL-GR
- dpv_loc_owl:NL-GR
is_a: NL
class_uri: loc:NL-GR

```
</details></div>