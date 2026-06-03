---
search:
  boost: 10.0
---

# Class: FR75C 


_Concept representing region Paris in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-75C](https://w3id.org/lmodel/dpv/loc/FR-75C)





```mermaid
 classDiagram
    class FR75C
    click FR75C href "../FR75C/"
      FR <|-- FR75C
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FR75C**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-75C](https://w3id.org/lmodel/dpv/loc/FR-75C) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-75C
* Paris




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-75C |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-75C |
| native | loc:FR75C |
| exact | dpv_loc:FR-75C, dpv_loc_owl:FR-75C |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FR75C
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-75C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Paris in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-75C
- Paris
exact_mappings:
- dpv_loc:FR-75C
- dpv_loc_owl:FR-75C
is_a: FR
class_uri: loc:FR-75C

```
</details>

### Induced

<details>
```yaml
name: FR75C
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-75C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Paris in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-75C
- Paris
exact_mappings:
- dpv_loc:FR-75C
- dpv_loc_owl:FR-75C
is_a: FR
class_uri: loc:FR-75C

```
</details></div>