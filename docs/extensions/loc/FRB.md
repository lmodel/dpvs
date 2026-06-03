---
search:
  boost: 10.0
---

# Class: FRB 


_Concept representing region Aquitaine in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-B](https://w3id.org/lmodel/dpv/loc/FR-B)





```mermaid
 classDiagram
    class FRB
    click FRB href "../FRB/"
      FR <|-- FRB
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-B](https://w3id.org/lmodel/dpv/loc/FR-B) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-B
* Aquitaine




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-B |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-B |
| native | loc:FRB |
| exact | dpv_loc:FR-B, dpv_loc_owl:FR-B |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-B
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Aquitaine in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-B
- Aquitaine
exact_mappings:
- dpv_loc:FR-B
- dpv_loc_owl:FR-B
is_a: FR
class_uri: loc:FR-B

```
</details>

### Induced

<details>
```yaml
name: FRB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-B
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Aquitaine in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-B
- Aquitaine
exact_mappings:
- dpv_loc:FR-B
- dpv_loc_owl:FR-B
is_a: FR
class_uri: loc:FR-B

```
</details></div>