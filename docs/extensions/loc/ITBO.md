---
search:
  boost: 10.0
---

# Class: ITBO 


_Concept representing region Metropolitan city of Bologna in country_

_Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-BO](https://w3id.org/lmodel/dpv/loc/IT-BO)





```mermaid
 classDiagram
    class ITBO
    click ITBO href "../ITBO/"
      IT <|-- ITBO
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITBO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-BO](https://w3id.org/lmodel/dpv/loc/IT-BO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-BO
* Metropolitan city of Bologna




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-BO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-BO |
| native | loc:ITBO |
| exact | dpv_loc:IT-BO, dpv_loc_owl:IT-BO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITBO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Metropolitan city of Bologna in country

  Italy'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BO
- Metropolitan city of Bologna
exact_mappings:
- dpv_loc:IT-BO
- dpv_loc_owl:IT-BO
is_a: IT
class_uri: loc:IT-BO

```
</details>

### Induced

<details>
```yaml
name: ITBO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Metropolitan city of Bologna in country

  Italy'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BO
- Metropolitan city of Bologna
exact_mappings:
- dpv_loc:IT-BO
- dpv_loc_owl:IT-BO
is_a: IT
class_uri: loc:IT-BO

```
</details></div>