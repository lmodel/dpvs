---
search:
  boost: 10.0
---

# Class: ITPC 


_Concept representing region Province of Piacenza in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PC](https://w3id.org/lmodel/dpv/loc/IT-PC)





```mermaid
 classDiagram
    class ITPC
    click ITPC href "../ITPC/"
      IT <|-- ITPC
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PC](https://w3id.org/lmodel/dpv/loc/IT-PC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PC
* Province of Piacenza




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PC |
| native | loc:ITPC |
| exact | dpv_loc:IT-PC, dpv_loc_owl:IT-PC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Piacenza in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PC
- Province of Piacenza
exact_mappings:
- dpv_loc:IT-PC
- dpv_loc_owl:IT-PC
is_a: IT
class_uri: loc:IT-PC

```
</details>

### Induced

<details>
```yaml
name: ITPC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Piacenza in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PC
- Province of Piacenza
exact_mappings:
- dpv_loc:IT-PC
- dpv_loc_owl:IT-PC
is_a: IT
class_uri: loc:IT-PC

```
</details></div>