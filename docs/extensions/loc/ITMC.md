---
search:
  boost: 10.0
---

# Class: ITMC 


_Concept representing region Province of Macerata in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-MC](https://w3id.org/lmodel/dpv/loc/IT-MC)





```mermaid
 classDiagram
    class ITMC
    click ITMC href "../ITMC/"
      IT <|-- ITMC
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITMC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-MC](https://w3id.org/lmodel/dpv/loc/IT-MC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-MC
* Province of Macerata




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-MC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-MC |
| native | loc:ITMC |
| exact | dpv_loc:IT-MC, dpv_loc_owl:IT-MC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITMC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Macerata in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MC
- Province of Macerata
exact_mappings:
- dpv_loc:IT-MC
- dpv_loc_owl:IT-MC
is_a: IT
class_uri: loc:IT-MC

```
</details>

### Induced

<details>
```yaml
name: ITMC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Macerata in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MC
- Province of Macerata
exact_mappings:
- dpv_loc:IT-MC
- dpv_loc_owl:IT-MC
is_a: IT
class_uri: loc:IT-MC

```
</details></div>