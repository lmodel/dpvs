---
search:
  boost: 10.0
---

# Class: TF 


_Concept representing Country of French Southern Territories_



<div data-search-exclude markdown="1">



URI: [loc:TF](https://w3id.org/lmodel/dpv/loc/TF)





```mermaid
 classDiagram
    class TF
    click TF href "../TF/"
      FR <|-- TF
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **TF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:TF](https://w3id.org/lmodel/dpv/loc/TF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* French Southern Territories




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#TF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:TF |
| native | loc:TF |
| exact | dpv_loc:TF, dpv_loc_owl:TF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of French Southern Territories
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- French Southern Territories
exact_mappings:
- dpv_loc:TF
- dpv_loc_owl:TF
is_a: FR
class_uri: loc:TF

```
</details>

### Induced

<details>
```yaml
name: TF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of French Southern Territories
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- French Southern Territories
exact_mappings:
- dpv_loc:TF
- dpv_loc_owl:TF
is_a: FR
class_uri: loc:TF

```
</details></div>