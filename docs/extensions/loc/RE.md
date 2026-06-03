---
search:
  boost: 10.0
---

# Class: RE 


_Concept representing Country of Réunion_



<div data-search-exclude markdown="1">



URI: [loc:RE](https://w3id.org/lmodel/dpv/loc/RE)





```mermaid
 classDiagram
    class RE
    click RE href "../RE/"
      FR <|-- RE
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **RE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RE](https://w3id.org/lmodel/dpv/loc/RE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Réunion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RE |
| native | loc:RE |
| exact | dpv_loc:RE, dpv_loc_owl:RE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Réunion
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Réunion
exact_mappings:
- dpv_loc:RE
- dpv_loc_owl:RE
is_a: FR
class_uri: loc:RE

```
</details>

### Induced

<details>
```yaml
name: RE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Réunion
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Réunion
exact_mappings:
- dpv_loc:RE
- dpv_loc_owl:RE
is_a: FR
class_uri: loc:RE

```
</details></div>