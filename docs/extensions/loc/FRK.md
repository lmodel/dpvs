---
search:
  boost: 10.0
---

# Class: FRK 


_Concept representing region Languedoc-Roussillon in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-K](https://w3id.org/lmodel/dpv/loc/FR-K)





```mermaid
 classDiagram
    class FRK
    click FRK href "../FRK/"
      FR <|-- FRK
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRK**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-K](https://w3id.org/lmodel/dpv/loc/FR-K) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-K
* Languedoc-Roussillon




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-K |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-K |
| native | loc:FRK |
| exact | dpv_loc:FR-K, dpv_loc_owl:FR-K |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-K
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Languedoc-Roussillon in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-K
- Languedoc-Roussillon
exact_mappings:
- dpv_loc:FR-K
- dpv_loc_owl:FR-K
is_a: FR
class_uri: loc:FR-K

```
</details>

### Induced

<details>
```yaml
name: FRK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-K
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Languedoc-Roussillon in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-K
- Languedoc-Roussillon
exact_mappings:
- dpv_loc:FR-K
- dpv_loc_owl:FR-K
is_a: FR
class_uri: loc:FR-K

```
</details></div>