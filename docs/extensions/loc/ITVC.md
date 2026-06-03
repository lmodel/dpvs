---
search:
  boost: 10.0
---

# Class: ITVC 


_Concept representing region Province of Vercelli in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-VC](https://w3id.org/lmodel/dpv/loc/IT-VC)





```mermaid
 classDiagram
    class ITVC
    click ITVC href "../ITVC/"
      IT <|-- ITVC
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITVC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-VC](https://w3id.org/lmodel/dpv/loc/IT-VC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-VC
* Province of Vercelli




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-VC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-VC |
| native | loc:ITVC |
| exact | dpv_loc:IT-VC, dpv_loc_owl:IT-VC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITVC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Vercelli in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VC
- Province of Vercelli
exact_mappings:
- dpv_loc:IT-VC
- dpv_loc_owl:IT-VC
is_a: IT
class_uri: loc:IT-VC

```
</details>

### Induced

<details>
```yaml
name: ITVC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Vercelli in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VC
- Province of Vercelli
exact_mappings:
- dpv_loc:IT-VC
- dpv_loc_owl:IT-VC
is_a: IT
class_uri: loc:IT-VC

```
</details></div>