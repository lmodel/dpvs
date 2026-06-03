---
search:
  boost: 10.0
---

# Class: YT 


_Concept representing Country of Mayotte_



<div data-search-exclude markdown="1">



URI: [loc:YT](https://w3id.org/lmodel/dpv/loc/YT)





```mermaid
 classDiagram
    class YT
    click YT href "../YT/"
      FR <|-- YT
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **YT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:YT](https://w3id.org/lmodel/dpv/loc/YT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Mayotte




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#YT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:YT |
| native | loc:YT |
| exact | dpv_loc:YT, dpv_loc_owl:YT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: YT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#YT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Mayotte
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Mayotte
exact_mappings:
- dpv_loc:YT
- dpv_loc_owl:YT
is_a: FR
class_uri: loc:YT

```
</details>

### Induced

<details>
```yaml
name: YT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#YT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Mayotte
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Mayotte
exact_mappings:
- dpv_loc:YT
- dpv_loc_owl:YT
is_a: FR
class_uri: loc:YT

```
</details></div>