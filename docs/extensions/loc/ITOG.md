---
search:
  boost: 10.0
---

# Class: ITOG 


_Concept representing region Province of Ogliastra in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-OG](https://w3id.org/lmodel/dpv/loc/IT-OG)





```mermaid
 classDiagram
    class ITOG
    click ITOG href "../ITOG/"
      IT <|-- ITOG
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITOG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-OG](https://w3id.org/lmodel/dpv/loc/IT-OG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-OG
* Province of Ogliastra




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-OG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-OG |
| native | loc:ITOG |
| exact | dpv_loc:IT-OG, dpv_loc_owl:IT-OG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITOG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-OG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ogliastra in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-OG
- Province of Ogliastra
exact_mappings:
- dpv_loc:IT-OG
- dpv_loc_owl:IT-OG
is_a: IT
class_uri: loc:IT-OG

```
</details>

### Induced

<details>
```yaml
name: ITOG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-OG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ogliastra in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-OG
- Province of Ogliastra
exact_mappings:
- dpv_loc:IT-OG
- dpv_loc_owl:IT-OG
is_a: IT
class_uri: loc:IT-OG

```
</details></div>