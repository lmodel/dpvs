---
search:
  boost: 10.0
---

# Class: ITCE 


_Concept representing region Province of Caserta in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-CE](https://w3id.org/lmodel/dpv/loc/IT-CE)





```mermaid
 classDiagram
    class ITCE
    click ITCE href "../ITCE/"
      IT <|-- ITCE
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITCE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-CE](https://w3id.org/lmodel/dpv/loc/IT-CE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-CE
* Province of Caserta




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-CE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-CE |
| native | loc:ITCE |
| exact | dpv_loc:IT-CE, dpv_loc_owl:IT-CE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITCE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Caserta in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CE
- Province of Caserta
exact_mappings:
- dpv_loc:IT-CE
- dpv_loc_owl:IT-CE
is_a: IT
class_uri: loc:IT-CE

```
</details>

### Induced

<details>
```yaml
name: ITCE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Caserta in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CE
- Province of Caserta
exact_mappings:
- dpv_loc:IT-CE
- dpv_loc_owl:IT-CE
is_a: IT
class_uri: loc:IT-CE

```
</details></div>