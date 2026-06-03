---
search:
  boost: 10.0
---

# Class: ITFM 


_Concept representing region Province of Fermo in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-FM](https://w3id.org/lmodel/dpv/loc/IT-FM)





```mermaid
 classDiagram
    class ITFM
    click ITFM href "../ITFM/"
      IT <|-- ITFM
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITFM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-FM](https://w3id.org/lmodel/dpv/loc/IT-FM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-FM
* Province of Fermo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-FM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-FM |
| native | loc:ITFM |
| exact | dpv_loc:IT-FM, dpv_loc_owl:IT-FM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITFM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-FM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Fermo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-FM
- Province of Fermo
exact_mappings:
- dpv_loc:IT-FM
- dpv_loc_owl:IT-FM
is_a: IT
class_uri: loc:IT-FM

```
</details>

### Induced

<details>
```yaml
name: ITFM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-FM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Fermo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-FM
- Province of Fermo
exact_mappings:
- dpv_loc:IT-FM
- dpv_loc_owl:IT-FM
is_a: IT
class_uri: loc:IT-FM

```
</details></div>