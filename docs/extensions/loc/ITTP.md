---
search:
  boost: 10.0
---

# Class: ITTP 


_Concept representing region Province of Trapani in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-TP](https://w3id.org/lmodel/dpv/loc/IT-TP)





```mermaid
 classDiagram
    class ITTP
    click ITTP href "../ITTP/"
      IT <|-- ITTP
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITTP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-TP](https://w3id.org/lmodel/dpv/loc/IT-TP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-TP
* Province of Trapani




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-TP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-TP |
| native | loc:ITTP |
| exact | dpv_loc:IT-TP, dpv_loc_owl:IT-TP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITTP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Trapani in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TP
- Province of Trapani
exact_mappings:
- dpv_loc:IT-TP
- dpv_loc_owl:IT-TP
is_a: IT
class_uri: loc:IT-TP

```
</details>

### Induced

<details>
```yaml
name: ITTP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Trapani in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TP
- Province of Trapani
exact_mappings:
- dpv_loc:IT-TP
- dpv_loc_owl:IT-TP
is_a: IT
class_uri: loc:IT-TP

```
</details></div>