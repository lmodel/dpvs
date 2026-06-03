---
search:
  boost: 10.0
---

# Class: MXMIC 


_Concept representing region Michoacán in country Mexico_



<div data-search-exclude markdown="1">



URI: [loc:MX-MIC](https://w3id.org/lmodel/dpv/loc/MX-MIC)





```mermaid
 classDiagram
    class MXMIC
    click MXMIC href "../MXMIC/"
      MX <|-- MXMIC
        click MX href "../MX/"
      
      
```





## Inheritance
* [MX](MX.md)
    * **MXMIC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MX-MIC](https://w3id.org/lmodel/dpv/loc/MX-MIC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* MX-MIC
* Michoacán




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MX-MIC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MX-MIC |
| native | loc:MXMIC |
| exact | dpv_loc:MX-MIC, dpv_loc_owl:MX-MIC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MXMIC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MX-MIC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Michoacán in country Mexico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MX-MIC
- Michoacán
exact_mappings:
- dpv_loc:MX-MIC
- dpv_loc_owl:MX-MIC
is_a: MX
class_uri: loc:MX-MIC

```
</details>

### Induced

<details>
```yaml
name: MXMIC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MX-MIC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Michoacán in country Mexico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MX-MIC
- Michoacán
exact_mappings:
- dpv_loc:MX-MIC
- dpv_loc_owl:MX-MIC
is_a: MX
class_uri: loc:MX-MIC

```
</details></div>