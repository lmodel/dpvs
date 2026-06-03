---
search:
  boost: 10.0
---

# Class: ITAG 


_Concept representing region Province of Agrigento in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-AG](https://w3id.org/lmodel/dpv/loc/IT-AG)





```mermaid
 classDiagram
    class ITAG
    click ITAG href "../ITAG/"
      IT <|-- ITAG
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITAG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-AG](https://w3id.org/lmodel/dpv/loc/IT-AG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-AG
* Province of Agrigento




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-AG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-AG |
| native | loc:ITAG |
| exact | dpv_loc:IT-AG, dpv_loc_owl:IT-AG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITAG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Agrigento in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AG
- Province of Agrigento
exact_mappings:
- dpv_loc:IT-AG
- dpv_loc_owl:IT-AG
is_a: IT
class_uri: loc:IT-AG

```
</details>

### Induced

<details>
```yaml
name: ITAG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Agrigento in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AG
- Province of Agrigento
exact_mappings:
- dpv_loc:IT-AG
- dpv_loc_owl:IT-AG
is_a: IT
class_uri: loc:IT-AG

```
</details></div>