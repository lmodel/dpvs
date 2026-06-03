---
search:
  boost: 10.0
---

# Class: FRBL 


_Concept representing region Saint-Barthélemy in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-BL](https://w3id.org/lmodel/dpv/loc/FR-BL)





```mermaid
 classDiagram
    class FRBL
    click FRBL href "../FRBL/"
      FR <|-- FRBL
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRBL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-BL](https://w3id.org/lmodel/dpv/loc/FR-BL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-BL
* Saint-Barthélemy




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-BL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-BL |
| native | loc:FRBL |
| exact | dpv_loc:FR-BL, dpv_loc_owl:FR-BL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRBL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-BL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saint-Barthélemy in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-BL
- Saint-Barthélemy
exact_mappings:
- dpv_loc:FR-BL
- dpv_loc_owl:FR-BL
is_a: FR
class_uri: loc:FR-BL

```
</details>

### Induced

<details>
```yaml
name: FRBL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-BL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saint-Barthélemy in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-BL
- Saint-Barthélemy
exact_mappings:
- dpv_loc:FR-BL
- dpv_loc_owl:FR-BL
is_a: FR
class_uri: loc:FR-BL

```
</details></div>