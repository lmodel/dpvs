---
search:
  boost: 10.0
---

# Class: ITMN 


_Concept representing region Province of Mantua in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-MN](https://w3id.org/lmodel/dpv/loc/IT-MN)





```mermaid
 classDiagram
    class ITMN
    click ITMN href "../ITMN/"
      IT <|-- ITMN
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITMN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-MN](https://w3id.org/lmodel/dpv/loc/IT-MN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-MN
* Province of Mantua




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-MN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-MN |
| native | loc:ITMN |
| exact | dpv_loc:IT-MN, dpv_loc_owl:IT-MN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Mantua in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MN
- Province of Mantua
exact_mappings:
- dpv_loc:IT-MN
- dpv_loc_owl:IT-MN
is_a: IT
class_uri: loc:IT-MN

```
</details>

### Induced

<details>
```yaml
name: ITMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Mantua in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MN
- Province of Mantua
exact_mappings:
- dpv_loc:IT-MN
- dpv_loc_owl:IT-MN
is_a: IT
class_uri: loc:IT-MN

```
</details></div>