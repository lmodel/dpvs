---
search:
  boost: 10.0
---

# Class: NLGE 


_Concept representing region Gelderland in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-GE](https://w3id.org/lmodel/dpv/loc/NL-GE)





```mermaid
 classDiagram
    class NLGE
    click NLGE href "../NLGE/"
      NL <|-- NLGE
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLGE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-GE](https://w3id.org/lmodel/dpv/loc/NL-GE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-GE
* Gelderland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-GE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-GE |
| native | loc:NLGE |
| exact | dpv_loc:NL-GE, dpv_loc_owl:NL-GE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLGE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-GE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gelderland in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-GE
- Gelderland
exact_mappings:
- dpv_loc:NL-GE
- dpv_loc_owl:NL-GE
is_a: NL
class_uri: loc:NL-GE

```
</details>

### Induced

<details>
```yaml
name: NLGE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-GE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Gelderland in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-GE
- Gelderland
exact_mappings:
- dpv_loc:NL-GE
- dpv_loc_owl:NL-GE
is_a: NL
class_uri: loc:NL-GE

```
</details></div>