---
search:
  boost: 10.0
---

# Class: ITAP 


_Concept representing region Province of Ascoli Piceno in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-AP](https://w3id.org/lmodel/dpv/loc/IT-AP)





```mermaid
 classDiagram
    class ITAP
    click ITAP href "../ITAP/"
      IT <|-- ITAP
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITAP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-AP](https://w3id.org/lmodel/dpv/loc/IT-AP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-AP
* Province of Ascoli Piceno




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-AP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-AP |
| native | loc:ITAP |
| exact | dpv_loc:IT-AP, dpv_loc_owl:IT-AP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITAP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ascoli Piceno in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AP
- Province of Ascoli Piceno
exact_mappings:
- dpv_loc:IT-AP
- dpv_loc_owl:IT-AP
is_a: IT
class_uri: loc:IT-AP

```
</details>

### Induced

<details>
```yaml
name: ITAP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ascoli Piceno in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AP
- Province of Ascoli Piceno
exact_mappings:
- dpv_loc:IT-AP
- dpv_loc_owl:IT-AP
is_a: IT
class_uri: loc:IT-AP

```
</details></div>