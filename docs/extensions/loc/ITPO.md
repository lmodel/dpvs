---
search:
  boost: 10.0
---

# Class: ITPO 


_Concept representing region Province of Prato in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PO](https://w3id.org/lmodel/dpv/loc/IT-PO)





```mermaid
 classDiagram
    class ITPO
    click ITPO href "../ITPO/"
      IT <|-- ITPO
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PO](https://w3id.org/lmodel/dpv/loc/IT-PO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PO
* Province of Prato




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PO |
| native | loc:ITPO |
| exact | dpv_loc:IT-PO, dpv_loc_owl:IT-PO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Prato in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PO
- Province of Prato
exact_mappings:
- dpv_loc:IT-PO
- dpv_loc_owl:IT-PO
is_a: IT
class_uri: loc:IT-PO

```
</details>

### Induced

<details>
```yaml
name: ITPO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Prato in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PO
- Province of Prato
exact_mappings:
- dpv_loc:IT-PO
- dpv_loc_owl:IT-PO
is_a: IT
class_uri: loc:IT-PO

```
</details></div>