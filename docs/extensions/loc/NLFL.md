---
search:
  boost: 10.0
---

# Class: NLFL 


_Concept representing region Flevoland in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-FL](https://w3id.org/lmodel/dpv/loc/NL-FL)





```mermaid
 classDiagram
    class NLFL
    click NLFL href "../NLFL/"
      NL <|-- NLFL
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLFL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-FL](https://w3id.org/lmodel/dpv/loc/NL-FL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-FL
* Flevoland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-FL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-FL |
| native | loc:NLFL |
| exact | dpv_loc:NL-FL, dpv_loc_owl:NL-FL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLFL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-FL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Flevoland in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-FL
- Flevoland
exact_mappings:
- dpv_loc:NL-FL
- dpv_loc_owl:NL-FL
is_a: NL
class_uri: loc:NL-FL

```
</details>

### Induced

<details>
```yaml
name: NLFL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-FL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Flevoland in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-FL
- Flevoland
exact_mappings:
- dpv_loc:NL-FL
- dpv_loc_owl:NL-FL
is_a: NL
class_uri: loc:NL-FL

```
</details></div>