---
search:
  boost: 10.0
---

# Class: FRS 


_Concept representing region Picardie in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-S](https://w3id.org/lmodel/dpv/loc/FR-S)





```mermaid
 classDiagram
    class FRS
    click FRS href "../FRS/"
      FR <|-- FRS
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-S](https://w3id.org/lmodel/dpv/loc/FR-S) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-S
* Picardie




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-S |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-S |
| native | loc:FRS |
| exact | dpv_loc:FR-S, dpv_loc_owl:FR-S |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-S
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Picardie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-S
- Picardie
exact_mappings:
- dpv_loc:FR-S
- dpv_loc_owl:FR-S
is_a: FR
class_uri: loc:FR-S

```
</details>

### Induced

<details>
```yaml
name: FRS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-S
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Picardie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-S
- Picardie
exact_mappings:
- dpv_loc:FR-S
- dpv_loc_owl:FR-S
is_a: FR
class_uri: loc:FR-S

```
</details></div>