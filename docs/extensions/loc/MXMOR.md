---
search:
  boost: 10.0
---

# Class: MXMOR 


_Concept representing region Morelos in country Mexico_



<div data-search-exclude markdown="1">



URI: [loc:MX-MOR](https://w3id.org/lmodel/dpv/loc/MX-MOR)





```mermaid
 classDiagram
    class MXMOR
    click MXMOR href "../MXMOR/"
      MX <|-- MXMOR
        click MX href "../MX/"
      
      
```





## Inheritance
* [MX](MX.md)
    * **MXMOR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MX-MOR](https://w3id.org/lmodel/dpv/loc/MX-MOR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* MX-MOR
* Morelos




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MX-MOR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MX-MOR |
| native | loc:MXMOR |
| exact | dpv_loc:MX-MOR, dpv_loc_owl:MX-MOR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MXMOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MX-MOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Morelos in country Mexico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MX-MOR
- Morelos
exact_mappings:
- dpv_loc:MX-MOR
- dpv_loc_owl:MX-MOR
is_a: MX
class_uri: loc:MX-MOR

```
</details>

### Induced

<details>
```yaml
name: MXMOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MX-MOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Morelos in country Mexico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MX-MOR
- Morelos
exact_mappings:
- dpv_loc:MX-MOR
- dpv_loc_owl:MX-MOR
is_a: MX
class_uri: loc:MX-MOR

```
</details></div>