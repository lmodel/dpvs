---
search:
  boost: 10.0
---

# Class: FRBFC 


_Concept representing region Bourgogne-Franche-Comté in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-BFC](https://w3id.org/lmodel/dpv/loc/FR-BFC)





```mermaid
 classDiagram
    class FRBFC
    click FRBFC href "../FRBFC/"
      FR <|-- FRBFC
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRBFC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-BFC](https://w3id.org/lmodel/dpv/loc/FR-BFC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-BFC
* Bourgogne-Franche-Comté




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-BFC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-BFC |
| native | loc:FRBFC |
| exact | dpv_loc:FR-BFC, dpv_loc_owl:FR-BFC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRBFC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-BFC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bourgogne-Franche-Comté in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-BFC
- Bourgogne-Franche-Comté
exact_mappings:
- dpv_loc:FR-BFC
- dpv_loc_owl:FR-BFC
is_a: FR
class_uri: loc:FR-BFC

```
</details>

### Induced

<details>
```yaml
name: FRBFC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-BFC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bourgogne-Franche-Comté in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-BFC
- Bourgogne-Franche-Comté
exact_mappings:
- dpv_loc:FR-BFC
- dpv_loc_owl:FR-BFC
is_a: FR
class_uri: loc:FR-BFC

```
</details></div>