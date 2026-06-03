---
search:
  boost: 10.0
---

# Class: ITPD 


_Concept representing region Province of Padua in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PD](https://w3id.org/lmodel/dpv/loc/IT-PD)





```mermaid
 classDiagram
    class ITPD
    click ITPD href "../ITPD/"
      IT <|-- ITPD
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PD](https://w3id.org/lmodel/dpv/loc/IT-PD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PD
* Province of Padua




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PD |
| native | loc:ITPD |
| exact | dpv_loc:IT-PD, dpv_loc_owl:IT-PD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Padua in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PD
- Province of Padua
exact_mappings:
- dpv_loc:IT-PD
- dpv_loc_owl:IT-PD
is_a: IT
class_uri: loc:IT-PD

```
</details>

### Induced

<details>
```yaml
name: ITPD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Padua in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PD
- Province of Padua
exact_mappings:
- dpv_loc:IT-PD
- dpv_loc_owl:IT-PD
is_a: IT
class_uri: loc:IT-PD

```
</details></div>