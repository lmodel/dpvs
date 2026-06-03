---
search:
  boost: 10.0
---

# Class: ITSA 


_Concept representing region Province of Salerno in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-SA](https://w3id.org/lmodel/dpv/loc/IT-SA)





```mermaid
 classDiagram
    class ITSA
    click ITSA href "../ITSA/"
      IT <|-- ITSA
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITSA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-SA](https://w3id.org/lmodel/dpv/loc/IT-SA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-SA
* Province of Salerno




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-SA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-SA |
| native | loc:ITSA |
| exact | dpv_loc:IT-SA, dpv_loc_owl:IT-SA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Salerno in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SA
- Province of Salerno
exact_mappings:
- dpv_loc:IT-SA
- dpv_loc_owl:IT-SA
is_a: IT
class_uri: loc:IT-SA

```
</details>

### Induced

<details>
```yaml
name: ITSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Salerno in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SA
- Province of Salerno
exact_mappings:
- dpv_loc:IT-SA
- dpv_loc_owl:IT-SA
is_a: IT
class_uri: loc:IT-SA

```
</details></div>