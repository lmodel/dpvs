---
search:
  boost: 10.0
---

# Class: ITBZ 


_Concept representing region South Tyrol in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-BZ](https://w3id.org/lmodel/dpv/loc/IT-BZ)





```mermaid
 classDiagram
    class ITBZ
    click ITBZ href "../ITBZ/"
      IT <|-- ITBZ
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITBZ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-BZ](https://w3id.org/lmodel/dpv/loc/IT-BZ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-BZ
* South Tyrol




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-BZ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-BZ |
| native | loc:ITBZ |
| exact | dpv_loc:IT-BZ, dpv_loc_owl:IT-BZ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITBZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BZ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region South Tyrol in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BZ
- South Tyrol
exact_mappings:
- dpv_loc:IT-BZ
- dpv_loc_owl:IT-BZ
is_a: IT
class_uri: loc:IT-BZ

```
</details>

### Induced

<details>
```yaml
name: ITBZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BZ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region South Tyrol in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BZ
- South Tyrol
exact_mappings:
- dpv_loc:IT-BZ
- dpv_loc_owl:IT-BZ
is_a: IT
class_uri: loc:IT-BZ

```
</details></div>