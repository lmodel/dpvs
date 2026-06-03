---
search:
  boost: 10.0
---

# Class: ITSP 


_Concept representing region Province of La Spezia in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-SP](https://w3id.org/lmodel/dpv/loc/IT-SP)





```mermaid
 classDiagram
    class ITSP
    click ITSP href "../ITSP/"
      IT <|-- ITSP
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITSP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-SP](https://w3id.org/lmodel/dpv/loc/IT-SP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-SP
* Province of La Spezia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-SP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-SP |
| native | loc:ITSP |
| exact | dpv_loc:IT-SP, dpv_loc_owl:IT-SP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITSP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of La Spezia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SP
- Province of La Spezia
exact_mappings:
- dpv_loc:IT-SP
- dpv_loc_owl:IT-SP
is_a: IT
class_uri: loc:IT-SP

```
</details>

### Induced

<details>
```yaml
name: ITSP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of La Spezia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SP
- Province of La Spezia
exact_mappings:
- dpv_loc:IT-SP
- dpv_loc_owl:IT-SP
is_a: IT
class_uri: loc:IT-SP

```
</details></div>