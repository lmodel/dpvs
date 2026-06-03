---
search:
  boost: 10.0
---

# Class: ITOR 


_Concept representing region Province of Oristano in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-OR](https://w3id.org/lmodel/dpv/loc/IT-OR)





```mermaid
 classDiagram
    class ITOR
    click ITOR href "../ITOR/"
      IT <|-- ITOR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITOR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-OR](https://w3id.org/lmodel/dpv/loc/IT-OR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-OR
* Province of Oristano




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-OR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-OR |
| native | loc:ITOR |
| exact | dpv_loc:IT-OR, dpv_loc_owl:IT-OR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-OR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Oristano in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-OR
- Province of Oristano
exact_mappings:
- dpv_loc:IT-OR
- dpv_loc_owl:IT-OR
is_a: IT
class_uri: loc:IT-OR

```
</details>

### Induced

<details>
```yaml
name: ITOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-OR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Oristano in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-OR
- Province of Oristano
exact_mappings:
- dpv_loc:IT-OR
- dpv_loc_owl:IT-OR
is_a: IT
class_uri: loc:IT-OR

```
</details></div>