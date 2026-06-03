---
search:
  boost: 10.0
---

# Class: ITVS 


_Concept representing region Province of Medio Campidano in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-VS](https://w3id.org/lmodel/dpv/loc/IT-VS)





```mermaid
 classDiagram
    class ITVS
    click ITVS href "../ITVS/"
      IT <|-- ITVS
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITVS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-VS](https://w3id.org/lmodel/dpv/loc/IT-VS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-VS
* Province of Medio Campidano




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-VS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-VS |
| native | loc:ITVS |
| exact | dpv_loc:IT-VS, dpv_loc_owl:IT-VS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITVS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Medio Campidano in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VS
- Province of Medio Campidano
exact_mappings:
- dpv_loc:IT-VS
- dpv_loc_owl:IT-VS
is_a: IT
class_uri: loc:IT-VS

```
</details>

### Induced

<details>
```yaml
name: ITVS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Medio Campidano in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VS
- Province of Medio Campidano
exact_mappings:
- dpv_loc:IT-VS
- dpv_loc_owl:IT-VS
is_a: IT
class_uri: loc:IT-VS

```
</details></div>