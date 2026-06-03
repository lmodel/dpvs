---
search:
  boost: 10.0
---

# Class: ITNU 


_Concept representing region Province of Nuoro in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-NU](https://w3id.org/lmodel/dpv/loc/IT-NU)





```mermaid
 classDiagram
    class ITNU
    click ITNU href "../ITNU/"
      IT <|-- ITNU
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITNU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-NU](https://w3id.org/lmodel/dpv/loc/IT-NU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-NU
* Province of Nuoro




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-NU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-NU |
| native | loc:ITNU |
| exact | dpv_loc:IT-NU, dpv_loc_owl:IT-NU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITNU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-NU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Nuoro in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-NU
- Province of Nuoro
exact_mappings:
- dpv_loc:IT-NU
- dpv_loc_owl:IT-NU
is_a: IT
class_uri: loc:IT-NU

```
</details>

### Induced

<details>
```yaml
name: ITNU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-NU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Nuoro in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-NU
- Province of Nuoro
exact_mappings:
- dpv_loc:IT-NU
- dpv_loc_owl:IT-NU
is_a: IT
class_uri: loc:IT-NU

```
</details></div>