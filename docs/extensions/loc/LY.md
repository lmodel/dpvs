---
search:
  boost: 10.0
---

# Class: LY 


_Concept representing Country of Libya_



<div data-search-exclude markdown="1">



URI: [loc:LY](https://w3id.org/lmodel/dpv/loc/LY)





```mermaid
 classDiagram
    class LY
    click LY href "../LY/"
      LY <|-- LYBA
        click LYBA href "../LYBA/"
      LY <|-- LYJA
        click LYJA href "../LYJA/"
      LY <|-- LYWD
        click LYWD href "../LYWD/"
      
      
```





## Inheritance
* **LY**
    * [LYBA](LYBA.md)
    * [LYJA](LYJA.md)
    * [LYWD](LYWD.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:LY](https://w3id.org/lmodel/dpv/loc/LY) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Libya




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#LY |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:LY |
| native | loc:LY |
| exact | dpv_loc:LY, dpv_loc_owl:LY |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Libya
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Libya
exact_mappings:
- dpv_loc:LY
- dpv_loc_owl:LY
class_uri: loc:LY

```
</details>

### Induced

<details>
```yaml
name: LY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#LY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Libya
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Libya
exact_mappings:
- dpv_loc:LY
- dpv_loc_owl:LY
class_uri: loc:LY

```
</details></div>