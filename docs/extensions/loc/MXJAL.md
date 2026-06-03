---
search:
  boost: 10.0
---

# Class: MXJAL 


_Concept representing region Jalisco in country Mexico_



<div data-search-exclude markdown="1">



URI: [loc:MX-JAL](https://w3id.org/lmodel/dpv/loc/MX-JAL)





```mermaid
 classDiagram
    class MXJAL
    click MXJAL href "../MXJAL/"
      MX <|-- MXJAL
        click MX href "../MX/"
      
      
```





## Inheritance
* [MX](MX.md)
    * **MXJAL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MX-JAL](https://w3id.org/lmodel/dpv/loc/MX-JAL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* MX-JAL
* Jalisco




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MX-JAL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MX-JAL |
| native | loc:MXJAL |
| exact | dpv_loc:MX-JAL, dpv_loc_owl:MX-JAL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MXJAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MX-JAL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Jalisco in country Mexico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MX-JAL
- Jalisco
exact_mappings:
- dpv_loc:MX-JAL
- dpv_loc_owl:MX-JAL
is_a: MX
class_uri: loc:MX-JAL

```
</details>

### Induced

<details>
```yaml
name: MXJAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MX-JAL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Jalisco in country Mexico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MX-JAL
- Jalisco
exact_mappings:
- dpv_loc:MX-JAL
- dpv_loc_owl:MX-JAL
is_a: MX
class_uri: loc:MX-JAL

```
</details></div>