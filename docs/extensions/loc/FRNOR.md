---
search:
  boost: 10.0
---

# Class: FRNOR 


_Concept representing region Normandie in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-NOR](https://w3id.org/lmodel/dpv/loc/FR-NOR)





```mermaid
 classDiagram
    class FRNOR
    click FRNOR href "../FRNOR/"
      FR <|-- FRNOR
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRNOR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-NOR](https://w3id.org/lmodel/dpv/loc/FR-NOR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-NOR
* Normandie




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-NOR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-NOR |
| native | loc:FRNOR |
| exact | dpv_loc:FR-NOR, dpv_loc_owl:FR-NOR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRNOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-NOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Normandie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-NOR
- Normandie
exact_mappings:
- dpv_loc:FR-NOR
- dpv_loc_owl:FR-NOR
is_a: FR
class_uri: loc:FR-NOR

```
</details>

### Induced

<details>
```yaml
name: FRNOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-NOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Normandie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-NOR
- Normandie
exact_mappings:
- dpv_loc:FR-NOR
- dpv_loc_owl:FR-NOR
is_a: FR
class_uri: loc:FR-NOR

```
</details></div>