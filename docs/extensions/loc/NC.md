---
search:
  boost: 10.0
---

# Class: NC 


_Concept representing Country of New Caledonia_



<div data-search-exclude markdown="1">



URI: [loc:NC](https://w3id.org/lmodel/dpv/loc/NC)





```mermaid
 classDiagram
    class NC
    click NC href "../NC/"
      FR <|-- NC
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NC](https://w3id.org/lmodel/dpv/loc/NC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* New Caledonia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NC |
| native | loc:NC |
| exact | dpv_loc:NC, dpv_loc_owl:NC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of New Caledonia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- New Caledonia
exact_mappings:
- dpv_loc:NC
- dpv_loc_owl:NC
is_a: FR
class_uri: loc:NC

```
</details>

### Induced

<details>
```yaml
name: NC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of New Caledonia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- New Caledonia
exact_mappings:
- dpv_loc:NC
- dpv_loc_owl:NC
is_a: FR
class_uri: loc:NC

```
</details></div>