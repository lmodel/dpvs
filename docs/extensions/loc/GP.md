---
search:
  boost: 10.0
---

# Class: GP 


_Concept representing Country of Guadeloupe_



<div data-search-exclude markdown="1">



URI: [loc:GP](https://w3id.org/lmodel/dpv/loc/GP)





```mermaid
 classDiagram
    class GP
    click GP href "../GP/"
      FR <|-- GP
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **GP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GP](https://w3id.org/lmodel/dpv/loc/GP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Guadeloupe




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GP |
| native | loc:GP |
| exact | dpv_loc:GP, dpv_loc_owl:GP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Guadeloupe
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Guadeloupe
exact_mappings:
- dpv_loc:GP
- dpv_loc_owl:GP
is_a: FR
class_uri: loc:GP

```
</details>

### Induced

<details>
```yaml
name: GP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Guadeloupe
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Guadeloupe
exact_mappings:
- dpv_loc:GP
- dpv_loc_owl:GP
is_a: FR
class_uri: loc:GP

```
</details></div>