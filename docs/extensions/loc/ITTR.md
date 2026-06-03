---
search:
  boost: 10.0
---

# Class: ITTR 


_Concept representing region Province of Terni in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-TR](https://w3id.org/lmodel/dpv/loc/IT-TR)





```mermaid
 classDiagram
    class ITTR
    click ITTR href "../ITTR/"
      IT <|-- ITTR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITTR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-TR](https://w3id.org/lmodel/dpv/loc/IT-TR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-TR
* Province of Terni




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-TR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-TR |
| native | loc:ITTR |
| exact | dpv_loc:IT-TR, dpv_loc_owl:IT-TR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITTR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Terni in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TR
- Province of Terni
exact_mappings:
- dpv_loc:IT-TR
- dpv_loc_owl:IT-TR
is_a: IT
class_uri: loc:IT-TR

```
</details>

### Induced

<details>
```yaml
name: ITTR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Terni in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TR
- Province of Terni
exact_mappings:
- dpv_loc:IT-TR
- dpv_loc_owl:IT-TR
is_a: IT
class_uri: loc:IT-TR

```
</details></div>