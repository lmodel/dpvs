---
search:
  boost: 10.0
---

# Class: ITSS 


_Concept representing region Province of Sassari in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-SS](https://w3id.org/lmodel/dpv/loc/IT-SS)





```mermaid
 classDiagram
    class ITSS
    click ITSS href "../ITSS/"
      IT <|-- ITSS
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITSS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-SS](https://w3id.org/lmodel/dpv/loc/IT-SS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-SS
* Province of Sassari




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-SS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-SS |
| native | loc:ITSS |
| exact | dpv_loc:IT-SS, dpv_loc_owl:IT-SS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITSS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Sassari in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SS
- Province of Sassari
exact_mappings:
- dpv_loc:IT-SS
- dpv_loc_owl:IT-SS
is_a: IT
class_uri: loc:IT-SS

```
</details>

### Induced

<details>
```yaml
name: ITSS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Sassari in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SS
- Province of Sassari
exact_mappings:
- dpv_loc:IT-SS
- dpv_loc_owl:IT-SS
is_a: IT
class_uri: loc:IT-SS

```
</details></div>