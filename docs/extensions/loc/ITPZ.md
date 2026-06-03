---
search:
  boost: 10.0
---

# Class: ITPZ 


_Concept representing region Province of Potenza in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PZ](https://w3id.org/lmodel/dpv/loc/IT-PZ)





```mermaid
 classDiagram
    class ITPZ
    click ITPZ href "../ITPZ/"
      IT <|-- ITPZ
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPZ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PZ](https://w3id.org/lmodel/dpv/loc/IT-PZ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PZ
* Province of Potenza




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PZ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PZ |
| native | loc:ITPZ |
| exact | dpv_loc:IT-PZ, dpv_loc_owl:IT-PZ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PZ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Potenza in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PZ
- Province of Potenza
exact_mappings:
- dpv_loc:IT-PZ
- dpv_loc_owl:IT-PZ
is_a: IT
class_uri: loc:IT-PZ

```
</details>

### Induced

<details>
```yaml
name: ITPZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PZ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Potenza in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PZ
- Province of Potenza
exact_mappings:
- dpv_loc:IT-PZ
- dpv_loc_owl:IT-PZ
is_a: IT
class_uri: loc:IT-PZ

```
</details></div>