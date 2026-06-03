---
search:
  boost: 10.0
---

# Class: ITRI 


_Concept representing region Province of Rieti in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-RI](https://w3id.org/lmodel/dpv/loc/IT-RI)





```mermaid
 classDiagram
    class ITRI
    click ITRI href "../ITRI/"
      IT <|-- ITRI
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITRI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-RI](https://w3id.org/lmodel/dpv/loc/IT-RI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-RI
* Province of Rieti




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-RI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-RI |
| native | loc:ITRI |
| exact | dpv_loc:IT-RI, dpv_loc_owl:IT-RI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITRI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-RI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Rieti in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-RI
- Province of Rieti
exact_mappings:
- dpv_loc:IT-RI
- dpv_loc_owl:IT-RI
is_a: IT
class_uri: loc:IT-RI

```
</details>

### Induced

<details>
```yaml
name: ITRI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-RI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Rieti in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-RI
- Province of Rieti
exact_mappings:
- dpv_loc:IT-RI
- dpv_loc_owl:IT-RI
is_a: IT
class_uri: loc:IT-RI

```
</details></div>