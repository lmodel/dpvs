---
search:
  boost: 10.0
---

# Class: NLUT 


_Concept representing region Utrecht (province) in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-UT](https://w3id.org/lmodel/dpv/loc/NL-UT)





```mermaid
 classDiagram
    class NLUT
    click NLUT href "../NLUT/"
      NL <|-- NLUT
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLUT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-UT](https://w3id.org/lmodel/dpv/loc/NL-UT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-UT
* Utrecht (province)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-UT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-UT |
| native | loc:NLUT |
| exact | dpv_loc:NL-UT, dpv_loc_owl:NL-UT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLUT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-UT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Utrecht (province) in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-UT
- Utrecht (province)
exact_mappings:
- dpv_loc:NL-UT
- dpv_loc_owl:NL-UT
is_a: NL
class_uri: loc:NL-UT

```
</details>

### Induced

<details>
```yaml
name: NLUT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-UT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Utrecht (province) in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-UT
- Utrecht (province)
exact_mappings:
- dpv_loc:NL-UT
- dpv_loc_owl:NL-UT
is_a: NL
class_uri: loc:NL-UT

```
</details></div>