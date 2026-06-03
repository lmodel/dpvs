---
search:
  boost: 10.0
---

# Class: MXMEX 


_Concept representing region Mexico (state) in country Mexico_



<div data-search-exclude markdown="1">



URI: [loc:MX-MEX](https://w3id.org/lmodel/dpv/loc/MX-MEX)





```mermaid
 classDiagram
    class MXMEX
    click MXMEX href "../MXMEX/"
      MX <|-- MXMEX
        click MX href "../MX/"
      
      
```





## Inheritance
* [MX](MX.md)
    * **MXMEX**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MX-MEX](https://w3id.org/lmodel/dpv/loc/MX-MEX) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* MX-MEX
* Mexico (state)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MX-MEX |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MX-MEX |
| native | loc:MXMEX |
| exact | dpv_loc:MX-MEX, dpv_loc_owl:MX-MEX |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MXMEX
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MX-MEX
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Mexico (state) in country Mexico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MX-MEX
- Mexico (state)
exact_mappings:
- dpv_loc:MX-MEX
- dpv_loc_owl:MX-MEX
is_a: MX
class_uri: loc:MX-MEX

```
</details>

### Induced

<details>
```yaml
name: MXMEX
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MX-MEX
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Mexico (state) in country Mexico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MX-MEX
- Mexico (state)
exact_mappings:
- dpv_loc:MX-MEX
- dpv_loc_owl:MX-MEX
is_a: MX
class_uri: loc:MX-MEX

```
</details></div>