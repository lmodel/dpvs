---
search:
  boost: 10.0
---

# Class: ITBS 


_Concept representing region Province of Brescia in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-BS](https://w3id.org/lmodel/dpv/loc/IT-BS)





```mermaid
 classDiagram
    class ITBS
    click ITBS href "../ITBS/"
      IT <|-- ITBS
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITBS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-BS](https://w3id.org/lmodel/dpv/loc/IT-BS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-BS
* Province of Brescia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-BS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-BS |
| native | loc:ITBS |
| exact | dpv_loc:IT-BS, dpv_loc_owl:IT-BS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITBS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Brescia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BS
- Province of Brescia
exact_mappings:
- dpv_loc:IT-BS
- dpv_loc_owl:IT-BS
is_a: IT
class_uri: loc:IT-BS

```
</details>

### Induced

<details>
```yaml
name: ITBS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Brescia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BS
- Province of Brescia
exact_mappings:
- dpv_loc:IT-BS
- dpv_loc_owl:IT-BS
is_a: IT
class_uri: loc:IT-BS

```
</details></div>