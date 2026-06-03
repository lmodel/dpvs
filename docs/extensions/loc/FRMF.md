---
search:
  boost: 10.0
---

# Class: FRMF 


_Concept representing region Saint-Martin (France) in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-MF](https://w3id.org/lmodel/dpv/loc/FR-MF)





```mermaid
 classDiagram
    class FRMF
    click FRMF href "../FRMF/"
      FR <|-- FRMF
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRMF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-MF](https://w3id.org/lmodel/dpv/loc/FR-MF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-MF
* Saint-Martin (France)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-MF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-MF |
| native | loc:FRMF |
| exact | dpv_loc:FR-MF, dpv_loc_owl:FR-MF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRMF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-MF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saint-Martin (France) in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-MF
- Saint-Martin (France)
exact_mappings:
- dpv_loc:FR-MF
- dpv_loc_owl:FR-MF
is_a: FR
class_uri: loc:FR-MF

```
</details>

### Induced

<details>
```yaml
name: FRMF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-MF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saint-Martin (France) in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-MF
- Saint-Martin (France)
exact_mappings:
- dpv_loc:FR-MF
- dpv_loc_owl:FR-MF
is_a: FR
class_uri: loc:FR-MF

```
</details></div>