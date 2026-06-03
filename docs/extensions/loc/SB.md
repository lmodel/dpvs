---
search:
  boost: 10.0
---

# Class: SB 


_Concept representing Country of Solomon Islands_



<div data-search-exclude markdown="1">



URI: [loc:SB](https://w3id.org/lmodel/dpv/loc/SB)





```mermaid
 classDiagram
    class SB
    click SB href "../SB/"
      SB <|-- SBCT
        click SBCT href "../SBCT/"
      SB <|-- SBMK
        click SBMK href "../SBMK/"
      SB <|-- SBWE
        click SBWE href "../SBWE/"
      
      
```





## Inheritance
* **SB**
    * [SBCT](SBCT.md)
    * [SBMK](SBMK.md)
    * [SBWE](SBWE.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SB](https://w3id.org/lmodel/dpv/loc/SB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Solomon Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SB |
| native | loc:SB |
| exact | dpv_loc:SB, dpv_loc_owl:SB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Solomon Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Solomon Islands
exact_mappings:
- dpv_loc:SB
- dpv_loc_owl:SB
class_uri: loc:SB

```
</details>

### Induced

<details>
```yaml
name: SB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Solomon Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Solomon Islands
exact_mappings:
- dpv_loc:SB
- dpv_loc_owl:SB
class_uri: loc:SB

```
</details></div>