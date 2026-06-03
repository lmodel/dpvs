---
search:
  boost: 10.0
---

# Class: ITAQ 


_Concept representing region Province of L'Aquila in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-AQ](https://w3id.org/lmodel/dpv/loc/IT-AQ)





```mermaid
 classDiagram
    class ITAQ
    click ITAQ href "../ITAQ/"
      IT <|-- ITAQ
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITAQ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-AQ](https://w3id.org/lmodel/dpv/loc/IT-AQ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-AQ
* Province of L'Aquila




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-AQ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-AQ |
| native | loc:ITAQ |
| exact | dpv_loc:IT-AQ, dpv_loc_owl:IT-AQ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITAQ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AQ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of L'Aquila in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AQ
- Province of L'Aquila
exact_mappings:
- dpv_loc:IT-AQ
- dpv_loc_owl:IT-AQ
is_a: IT
class_uri: loc:IT-AQ

```
</details>

### Induced

<details>
```yaml
name: ITAQ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AQ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of L'Aquila in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AQ
- Province of L'Aquila
exact_mappings:
- dpv_loc:IT-AQ
- dpv_loc_owl:IT-AQ
is_a: IT
class_uri: loc:IT-AQ

```
</details></div>