---
search:
  boost: 10.0
---

# Class: NLLI 


_Concept representing region Limburg (Netherlands) in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-LI](https://w3id.org/lmodel/dpv/loc/NL-LI)





```mermaid
 classDiagram
    class NLLI
    click NLLI href "../NLLI/"
      NL <|-- NLLI
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLLI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-LI](https://w3id.org/lmodel/dpv/loc/NL-LI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-LI
* Limburg (Netherlands)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-LI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-LI |
| native | loc:NLLI |
| exact | dpv_loc:NL-LI, dpv_loc_owl:NL-LI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLLI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-LI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Limburg (Netherlands) in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-LI
- Limburg (Netherlands)
exact_mappings:
- dpv_loc:NL-LI
- dpv_loc_owl:NL-LI
is_a: NL
class_uri: loc:NL-LI

```
</details>

### Induced

<details>
```yaml
name: NLLI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-LI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Limburg (Netherlands) in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-LI
- Limburg (Netherlands)
exact_mappings:
- dpv_loc:NL-LI
- dpv_loc_owl:NL-LI
is_a: NL
class_uri: loc:NL-LI

```
</details></div>