---
search:
  boost: 10.0
---

# Class: ITSR 


_Concept representing region Province of Syracuse in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-SR](https://w3id.org/lmodel/dpv/loc/IT-SR)





```mermaid
 classDiagram
    class ITSR
    click ITSR href "../ITSR/"
      IT <|-- ITSR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITSR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-SR](https://w3id.org/lmodel/dpv/loc/IT-SR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-SR
* Province of Syracuse




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-SR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-SR |
| native | loc:ITSR |
| exact | dpv_loc:IT-SR, dpv_loc_owl:IT-SR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITSR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Syracuse in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SR
- Province of Syracuse
exact_mappings:
- dpv_loc:IT-SR
- dpv_loc_owl:IT-SR
is_a: IT
class_uri: loc:IT-SR

```
</details>

### Induced

<details>
```yaml
name: ITSR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Syracuse in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SR
- Province of Syracuse
exact_mappings:
- dpv_loc:IT-SR
- dpv_loc_owl:IT-SR
is_a: IT
class_uri: loc:IT-SR

```
</details></div>