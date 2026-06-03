---
search:
  boost: 10.0
---

# Class: FRTF 


_Concept representing region French Southern and Antarctic Lands in_

_country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-TF](https://w3id.org/lmodel/dpv/loc/FR-TF)





```mermaid
 classDiagram
    class FRTF
    click FRTF href "../FRTF/"
      FR <|-- FRTF
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRTF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-TF](https://w3id.org/lmodel/dpv/loc/FR-TF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-TF
* French Southern and Antarctic Lands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-TF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-TF |
| native | loc:FRTF |
| exact | dpv_loc:FR-TF, dpv_loc_owl:FR-TF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRTF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-TF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region French Southern and Antarctic Lands in

  country France'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-TF
- French Southern and Antarctic Lands
exact_mappings:
- dpv_loc:FR-TF
- dpv_loc_owl:FR-TF
is_a: FR
class_uri: loc:FR-TF

```
</details>

### Induced

<details>
```yaml
name: FRTF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-TF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region French Southern and Antarctic Lands in

  country France'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-TF
- French Southern and Antarctic Lands
exact_mappings:
- dpv_loc:FR-TF
- dpv_loc_owl:FR-TF
is_a: FR
class_uri: loc:FR-TF

```
</details></div>