---
search:
  boost: 10.0
---

# Class: DKGL 


_Concept representing region Greenland in country Denmark_



<div data-search-exclude markdown="1">



URI: [loc:DK-GL](https://w3id.org/lmodel/dpv/loc/DK-GL)





```mermaid
 classDiagram
    class DKGL
    click DKGL href "../DKGL/"
      DK <|-- DKGL
        click DK href "../DK/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DK](DK.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DKGL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DK-GL](https://w3id.org/lmodel/dpv/loc/DK-GL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DK-GL
* Greenland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DK-GL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DK-GL |
| native | loc:DKGL |
| exact | dpv_loc:DK-GL, dpv_loc_owl:DK-GL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DKGL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DK-GL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Greenland in country Denmark
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DK-GL
- Greenland
exact_mappings:
- dpv_loc:DK-GL
- dpv_loc_owl:DK-GL
is_a: DK
class_uri: loc:DK-GL

```
</details>

### Induced

<details>
```yaml
name: DKGL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DK-GL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Greenland in country Denmark
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DK-GL
- Greenland
exact_mappings:
- dpv_loc:DK-GL
- dpv_loc_owl:DK-GL
is_a: DK
class_uri: loc:DK-GL

```
</details></div>