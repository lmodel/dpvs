---
search:
  boost: 10.0
---

# Class: NLAW 


_Concept representing region Aruba in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-AW](https://w3id.org/lmodel/dpv/loc/NL-AW)





```mermaid
 classDiagram
    class NLAW
    click NLAW href "../NLAW/"
      NL <|-- NLAW
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLAW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-AW](https://w3id.org/lmodel/dpv/loc/NL-AW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-AW
* Aruba




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-AW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-AW |
| native | loc:NLAW |
| exact | dpv_loc:NL-AW, dpv_loc_owl:NL-AW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLAW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-AW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Aruba in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-AW
- Aruba
exact_mappings:
- dpv_loc:NL-AW
- dpv_loc_owl:NL-AW
is_a: NL
class_uri: loc:NL-AW

```
</details>

### Induced

<details>
```yaml
name: NLAW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-AW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Aruba in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-AW
- Aruba
exact_mappings:
- dpv_loc:NL-AW
- dpv_loc_owl:NL-AW
is_a: NL
class_uri: loc:NL-AW

```
</details></div>