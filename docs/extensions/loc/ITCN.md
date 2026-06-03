---
search:
  boost: 10.0
---

# Class: ITCN 


_Concept representing region Province of Cuneo in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-CN](https://w3id.org/lmodel/dpv/loc/IT-CN)





```mermaid
 classDiagram
    class ITCN
    click ITCN href "../ITCN/"
      IT <|-- ITCN
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITCN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-CN](https://w3id.org/lmodel/dpv/loc/IT-CN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-CN
* Province of Cuneo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-CN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-CN |
| native | loc:ITCN |
| exact | dpv_loc:IT-CN, dpv_loc_owl:IT-CN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITCN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cuneo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CN
- Province of Cuneo
exact_mappings:
- dpv_loc:IT-CN
- dpv_loc_owl:IT-CN
is_a: IT
class_uri: loc:IT-CN

```
</details>

### Induced

<details>
```yaml
name: ITCN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cuneo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CN
- Province of Cuneo
exact_mappings:
- dpv_loc:IT-CN
- dpv_loc_owl:IT-CN
is_a: IT
class_uri: loc:IT-CN

```
</details></div>