---
search:
  boost: 10.0
---

# Class: ITVI 


_Concept representing region Province of Vicenza in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-VI](https://w3id.org/lmodel/dpv/loc/IT-VI)





```mermaid
 classDiagram
    class ITVI
    click ITVI href "../ITVI/"
      IT <|-- ITVI
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITVI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-VI](https://w3id.org/lmodel/dpv/loc/IT-VI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-VI
* Province of Vicenza




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-VI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-VI |
| native | loc:ITVI |
| exact | dpv_loc:IT-VI, dpv_loc_owl:IT-VI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITVI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Vicenza in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VI
- Province of Vicenza
exact_mappings:
- dpv_loc:IT-VI
- dpv_loc_owl:IT-VI
is_a: IT
class_uri: loc:IT-VI

```
</details>

### Induced

<details>
```yaml
name: ITVI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Vicenza in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VI
- Province of Vicenza
exact_mappings:
- dpv_loc:IT-VI
- dpv_loc_owl:IT-VI
is_a: IT
class_uri: loc:IT-VI

```
</details></div>