---
search:
  boost: 10.0
---

# Class: ITSO 


_Concept representing region Province of Sondrio in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-SO](https://w3id.org/lmodel/dpv/loc/IT-SO)





```mermaid
 classDiagram
    class ITSO
    click ITSO href "../ITSO/"
      IT <|-- ITSO
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITSO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-SO](https://w3id.org/lmodel/dpv/loc/IT-SO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-SO
* Province of Sondrio




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-SO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-SO |
| native | loc:ITSO |
| exact | dpv_loc:IT-SO, dpv_loc_owl:IT-SO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITSO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Sondrio in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SO
- Province of Sondrio
exact_mappings:
- dpv_loc:IT-SO
- dpv_loc_owl:IT-SO
is_a: IT
class_uri: loc:IT-SO

```
</details>

### Induced

<details>
```yaml
name: ITSO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Sondrio in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SO
- Province of Sondrio
exact_mappings:
- dpv_loc:IT-SO
- dpv_loc_owl:IT-SO
is_a: IT
class_uri: loc:IT-SO

```
</details></div>