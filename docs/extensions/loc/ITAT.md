---
search:
  boost: 10.0
---

# Class: ITAT 


_Concept representing region Province of Asti in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-AT](https://w3id.org/lmodel/dpv/loc/IT-AT)





```mermaid
 classDiagram
    class ITAT
    click ITAT href "../ITAT/"
      IT <|-- ITAT
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITAT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-AT](https://w3id.org/lmodel/dpv/loc/IT-AT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-AT
* Province of Asti




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-AT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-AT |
| native | loc:ITAT |
| exact | dpv_loc:IT-AT, dpv_loc_owl:IT-AT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITAT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Asti in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AT
- Province of Asti
exact_mappings:
- dpv_loc:IT-AT
- dpv_loc_owl:IT-AT
is_a: IT
class_uri: loc:IT-AT

```
</details>

### Induced

<details>
```yaml
name: ITAT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Asti in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AT
- Province of Asti
exact_mappings:
- dpv_loc:IT-AT
- dpv_loc_owl:IT-AT
is_a: IT
class_uri: loc:IT-AT

```
</details></div>