---
search:
  boost: 10.0
---

# Class: MUPL 


_Concept representing region Port Louis District in country Mauritius_



<div data-search-exclude markdown="1">



URI: [loc:MU-PL](https://w3id.org/lmodel/dpv/loc/MU-PL)





```mermaid
 classDiagram
    class MUPL
    click MUPL href "../MUPL/"
      MU <|-- MUPL
        click MU href "../MU/"
      
      
```





## Inheritance
* [MU](MU.md)
    * **MUPL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MU-PL](https://w3id.org/lmodel/dpv/loc/MU-PL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* MU-PL
* Port Louis District




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MU-PL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MU-PL |
| native | loc:MUPL |
| exact | dpv_loc:MU-PL, dpv_loc_owl:MU-PL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MUPL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MU-PL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Port Louis District in country Mauritius
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MU-PL
- Port Louis District
exact_mappings:
- dpv_loc:MU-PL
- dpv_loc_owl:MU-PL
is_a: MU
class_uri: loc:MU-PL

```
</details>

### Induced

<details>
```yaml
name: MUPL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MU-PL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Port Louis District in country Mauritius
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MU-PL
- Port Louis District
exact_mappings:
- dpv_loc:MU-PL
- dpv_loc_owl:MU-PL
is_a: MU
class_uri: loc:MU-PL

```
</details></div>