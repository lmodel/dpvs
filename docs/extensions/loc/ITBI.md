---
search:
  boost: 10.0
---

# Class: ITBI 


_Concept representing region Province of Biella in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-BI](https://w3id.org/lmodel/dpv/loc/IT-BI)





```mermaid
 classDiagram
    class ITBI
    click ITBI href "../ITBI/"
      IT <|-- ITBI
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITBI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-BI](https://w3id.org/lmodel/dpv/loc/IT-BI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-BI
* Province of Biella




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-BI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-BI |
| native | loc:ITBI |
| exact | dpv_loc:IT-BI, dpv_loc_owl:IT-BI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITBI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Biella in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BI
- Province of Biella
exact_mappings:
- dpv_loc:IT-BI
- dpv_loc_owl:IT-BI
is_a: IT
class_uri: loc:IT-BI

```
</details>

### Induced

<details>
```yaml
name: ITBI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Biella in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BI
- Province of Biella
exact_mappings:
- dpv_loc:IT-BI
- dpv_loc_owl:IT-BI
is_a: IT
class_uri: loc:IT-BI

```
</details></div>