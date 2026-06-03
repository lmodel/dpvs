---
search:
  boost: 10.0
---

# Class: FRQ 


_Concept representing region Haute-Normandie in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-Q](https://w3id.org/lmodel/dpv/loc/FR-Q)





```mermaid
 classDiagram
    class FRQ
    click FRQ href "../FRQ/"
      FR <|-- FRQ
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRQ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-Q](https://w3id.org/lmodel/dpv/loc/FR-Q) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-Q
* Haute-Normandie




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-Q |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-Q |
| native | loc:FRQ |
| exact | dpv_loc:FR-Q, dpv_loc_owl:FR-Q |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRQ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-Q
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Haute-Normandie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-Q
- Haute-Normandie
exact_mappings:
- dpv_loc:FR-Q
- dpv_loc_owl:FR-Q
is_a: FR
class_uri: loc:FR-Q

```
</details>

### Induced

<details>
```yaml
name: FRQ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-Q
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Haute-Normandie in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-Q
- Haute-Normandie
exact_mappings:
- dpv_loc:FR-Q
- dpv_loc_owl:FR-Q
is_a: FR
class_uri: loc:FR-Q

```
</details></div>