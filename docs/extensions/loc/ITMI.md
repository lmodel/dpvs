---
search:
  boost: 10.0
---

# Class: ITMI 


_Concept representing region Metropolitan city of Milan in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-MI](https://w3id.org/lmodel/dpv/loc/IT-MI)





```mermaid
 classDiagram
    class ITMI
    click ITMI href "../ITMI/"
      IT <|-- ITMI
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITMI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-MI](https://w3id.org/lmodel/dpv/loc/IT-MI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-MI
* Metropolitan city of Milan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-MI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-MI |
| native | loc:ITMI |
| exact | dpv_loc:IT-MI, dpv_loc_owl:IT-MI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITMI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Metropolitan city of Milan in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MI
- Metropolitan city of Milan
exact_mappings:
- dpv_loc:IT-MI
- dpv_loc_owl:IT-MI
is_a: IT
class_uri: loc:IT-MI

```
</details>

### Induced

<details>
```yaml
name: ITMI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Metropolitan city of Milan in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MI
- Metropolitan city of Milan
exact_mappings:
- dpv_loc:IT-MI
- dpv_loc_owl:IT-MI
is_a: IT
class_uri: loc:IT-MI

```
</details></div>