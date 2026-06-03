---
search:
  boost: 10.0
---

# Class: FRARA 


_Concept representing region Auvergne-Rhône-Alpes in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-ARA](https://w3id.org/lmodel/dpv/loc/FR-ARA)





```mermaid
 classDiagram
    class FRARA
    click FRARA href "../FRARA/"
      FR <|-- FRARA
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRARA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-ARA](https://w3id.org/lmodel/dpv/loc/FR-ARA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-ARA
* Auvergne-Rhône-Alpes




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-ARA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-ARA |
| native | loc:FRARA |
| exact | dpv_loc:FR-ARA, dpv_loc_owl:FR-ARA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRARA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-ARA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Auvergne-Rhône-Alpes in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-ARA
- Auvergne-Rhône-Alpes
exact_mappings:
- dpv_loc:FR-ARA
- dpv_loc_owl:FR-ARA
is_a: FR
class_uri: loc:FR-ARA

```
</details>

### Induced

<details>
```yaml
name: FRARA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-ARA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Auvergne-Rhône-Alpes in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-ARA
- Auvergne-Rhône-Alpes
exact_mappings:
- dpv_loc:FR-ARA
- dpv_loc_owl:FR-ARA
is_a: FR
class_uri: loc:FR-ARA

```
</details></div>