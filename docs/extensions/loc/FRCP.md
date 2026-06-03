---
search:
  boost: 10.0
---

# Class: FRCP 


_Concept representing region Clipperton Island in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-CP](https://w3id.org/lmodel/dpv/loc/FR-CP)





```mermaid
 classDiagram
    class FRCP
    click FRCP href "../FRCP/"
      FR <|-- FRCP
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRCP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-CP](https://w3id.org/lmodel/dpv/loc/FR-CP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-CP
* Clipperton Island




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-CP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-CP |
| native | loc:FRCP |
| exact | dpv_loc:FR-CP, dpv_loc_owl:FR-CP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRCP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-CP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Clipperton Island in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-CP
- Clipperton Island
exact_mappings:
- dpv_loc:FR-CP
- dpv_loc_owl:FR-CP
is_a: FR
class_uri: loc:FR-CP

```
</details>

### Induced

<details>
```yaml
name: FRCP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-CP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Clipperton Island in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-CP
- Clipperton Island
exact_mappings:
- dpv_loc:FR-CP
- dpv_loc_owl:FR-CP
is_a: FR
class_uri: loc:FR-CP

```
</details></div>