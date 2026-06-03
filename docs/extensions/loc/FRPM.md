---
search:
  boost: 10.0
---

# Class: FRPM 


_Concept representing region Saint-Pierre and Miquelon in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-PM](https://w3id.org/lmodel/dpv/loc/FR-PM)





```mermaid
 classDiagram
    class FRPM
    click FRPM href "../FRPM/"
      FR <|-- FRPM
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRPM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-PM](https://w3id.org/lmodel/dpv/loc/FR-PM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-PM
* Saint-Pierre and Miquelon




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-PM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-PM |
| native | loc:FRPM |
| exact | dpv_loc:FR-PM, dpv_loc_owl:FR-PM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRPM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-PM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saint-Pierre and Miquelon in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-PM
- Saint-Pierre and Miquelon
exact_mappings:
- dpv_loc:FR-PM
- dpv_loc_owl:FR-PM
is_a: FR
class_uri: loc:FR-PM

```
</details>

### Induced

<details>
```yaml
name: FRPM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-PM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saint-Pierre and Miquelon in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-PM
- Saint-Pierre and Miquelon
exact_mappings:
- dpv_loc:FR-PM
- dpv_loc_owl:FR-PM
is_a: FR
class_uri: loc:FR-PM

```
</details></div>