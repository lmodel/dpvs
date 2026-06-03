---
search:
  boost: 10.0
---

# Class: ITMO 


_Concept representing region Province of Modena in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-MO](https://w3id.org/lmodel/dpv/loc/IT-MO)





```mermaid
 classDiagram
    class ITMO
    click ITMO href "../ITMO/"
      IT <|-- ITMO
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITMO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-MO](https://w3id.org/lmodel/dpv/loc/IT-MO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-MO
* Province of Modena




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-MO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-MO |
| native | loc:ITMO |
| exact | dpv_loc:IT-MO, dpv_loc_owl:IT-MO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Modena in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MO
- Province of Modena
exact_mappings:
- dpv_loc:IT-MO
- dpv_loc_owl:IT-MO
is_a: IT
class_uri: loc:IT-MO

```
</details>

### Induced

<details>
```yaml
name: ITMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Modena in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MO
- Province of Modena
exact_mappings:
- dpv_loc:IT-MO
- dpv_loc_owl:IT-MO
is_a: IT
class_uri: loc:IT-MO

```
</details></div>