---
search:
  boost: 10.0
---

# Class: FRP 


_Concept representing region Basse-Normandie in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-P](https://w3id.org/lmodel/dpv/loc/FR-P)





```mermaid
 classDiagram
    class FRP
    click FRP href "../FRP/"
      FR <|-- FRP
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-P](https://w3id.org/lmodel/dpv/loc/FR-P) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-P
* Basse-Normandie




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-P |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-P |
| native | loc:FRP |
| exact | dpv_loc:FR-P, dpv_loc_owl:FR-P |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-P
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Basse-Normandie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-P
- Basse-Normandie
exact_mappings:
- dpv_loc:FR-P
- dpv_loc_owl:FR-P
is_a: FR
class_uri: loc:FR-P

```
</details>

### Induced

<details>
```yaml
name: FRP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-P
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Basse-Normandie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-P
- Basse-Normandie
exact_mappings:
- dpv_loc:FR-P
- dpv_loc_owl:FR-P
is_a: FR
class_uri: loc:FR-P

```
</details></div>