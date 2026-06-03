---
search:
  boost: 10.0
---

# Class: ITRM 


_Concept representing region Metropolitan city of Rome in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-RM](https://w3id.org/lmodel/dpv/loc/IT-RM)





```mermaid
 classDiagram
    class ITRM
    click ITRM href "../ITRM/"
      IT <|-- ITRM
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITRM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-RM](https://w3id.org/lmodel/dpv/loc/IT-RM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-RM
* Metropolitan city of Rome




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-RM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-RM |
| native | loc:ITRM |
| exact | dpv_loc:IT-RM, dpv_loc_owl:IT-RM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITRM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-RM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Metropolitan city of Rome in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-RM
- Metropolitan city of Rome
exact_mappings:
- dpv_loc:IT-RM
- dpv_loc_owl:IT-RM
is_a: IT
class_uri: loc:IT-RM

```
</details>

### Induced

<details>
```yaml
name: ITRM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-RM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Metropolitan city of Rome in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-RM
- Metropolitan city of Rome
exact_mappings:
- dpv_loc:IT-RM
- dpv_loc_owl:IT-RM
is_a: IT
class_uri: loc:IT-RM

```
</details></div>