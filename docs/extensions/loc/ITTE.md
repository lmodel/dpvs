---
search:
  boost: 10.0
---

# Class: ITTE 


_Concept representing region Province of Teramo in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-TE](https://w3id.org/lmodel/dpv/loc/IT-TE)





```mermaid
 classDiagram
    class ITTE
    click ITTE href "../ITTE/"
      IT <|-- ITTE
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITTE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-TE](https://w3id.org/lmodel/dpv/loc/IT-TE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-TE
* Province of Teramo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-TE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-TE |
| native | loc:ITTE |
| exact | dpv_loc:IT-TE, dpv_loc_owl:IT-TE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITTE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Teramo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TE
- Province of Teramo
exact_mappings:
- dpv_loc:IT-TE
- dpv_loc_owl:IT-TE
is_a: IT
class_uri: loc:IT-TE

```
</details>

### Induced

<details>
```yaml
name: ITTE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Teramo in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TE
- Province of Teramo
exact_mappings:
- dpv_loc:IT-TE
- dpv_loc_owl:IT-TE
is_a: IT
class_uri: loc:IT-TE

```
</details></div>