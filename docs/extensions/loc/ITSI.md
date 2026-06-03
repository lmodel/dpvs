---
search:
  boost: 10.0
---

# Class: ITSI 


_Concept representing region Province of Siena in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-SI](https://w3id.org/lmodel/dpv/loc/IT-SI)





```mermaid
 classDiagram
    class ITSI
    click ITSI href "../ITSI/"
      IT <|-- ITSI
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITSI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-SI](https://w3id.org/lmodel/dpv/loc/IT-SI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-SI
* Province of Siena




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-SI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-SI |
| native | loc:ITSI |
| exact | dpv_loc:IT-SI, dpv_loc_owl:IT-SI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITSI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Siena in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SI
- Province of Siena
exact_mappings:
- dpv_loc:IT-SI
- dpv_loc_owl:IT-SI
is_a: IT
class_uri: loc:IT-SI

```
</details>

### Induced

<details>
```yaml
name: ITSI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Siena in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SI
- Province of Siena
exact_mappings:
- dpv_loc:IT-SI
- dpv_loc_owl:IT-SI
is_a: IT
class_uri: loc:IT-SI

```
</details></div>