---
search:
  boost: 10.0
---

# Class: ITCB 


_Concept representing region Province of Campobasso in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-CB](https://w3id.org/lmodel/dpv/loc/IT-CB)





```mermaid
 classDiagram
    class ITCB
    click ITCB href "../ITCB/"
      IT <|-- ITCB
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITCB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-CB](https://w3id.org/lmodel/dpv/loc/IT-CB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-CB
* Province of Campobasso




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-CB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-CB |
| native | loc:ITCB |
| exact | dpv_loc:IT-CB, dpv_loc_owl:IT-CB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITCB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Campobasso in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CB
- Province of Campobasso
exact_mappings:
- dpv_loc:IT-CB
- dpv_loc_owl:IT-CB
is_a: IT
class_uri: loc:IT-CB

```
</details>

### Induced

<details>
```yaml
name: ITCB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Campobasso in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CB
- Province of Campobasso
exact_mappings:
- dpv_loc:IT-CB
- dpv_loc_owl:IT-CB
is_a: IT
class_uri: loc:IT-CB

```
</details></div>