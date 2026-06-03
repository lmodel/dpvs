---
search:
  boost: 10.0
---

# Class: FRPF 


_Concept representing region French Polynesia in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-PF](https://w3id.org/lmodel/dpv/loc/FR-PF)





```mermaid
 classDiagram
    class FRPF
    click FRPF href "../FRPF/"
      FR <|-- FRPF
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRPF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-PF](https://w3id.org/lmodel/dpv/loc/FR-PF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-PF
* French Polynesia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-PF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-PF |
| native | loc:FRPF |
| exact | dpv_loc:FR-PF, dpv_loc_owl:FR-PF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRPF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-PF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region French Polynesia in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-PF
- French Polynesia
exact_mappings:
- dpv_loc:FR-PF
- dpv_loc_owl:FR-PF
is_a: FR
class_uri: loc:FR-PF

```
</details>

### Induced

<details>
```yaml
name: FRPF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-PF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region French Polynesia in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-PF
- French Polynesia
exact_mappings:
- dpv_loc:FR-PF
- dpv_loc_owl:FR-PF
is_a: FR
class_uri: loc:FR-PF

```
</details></div>