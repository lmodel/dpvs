---
search:
  boost: 10.0
---

# Class: FRN 


_Concept representing region Midi-Pyrénées in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-N](https://w3id.org/lmodel/dpv/loc/FR-N)





```mermaid
 classDiagram
    class FRN
    click FRN href "../FRN/"
      FR <|-- FRN
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-N](https://w3id.org/lmodel/dpv/loc/FR-N) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-N
* Midi-Pyrénées




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-N |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-N |
| native | loc:FRN |
| exact | dpv_loc:FR-N, dpv_loc_owl:FR-N |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-N
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Midi-Pyrénées in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-N
- Midi-Pyrénées
exact_mappings:
- dpv_loc:FR-N
- dpv_loc_owl:FR-N
is_a: FR
class_uri: loc:FR-N

```
</details>

### Induced

<details>
```yaml
name: FRN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-N
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Midi-Pyrénées in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-N
- Midi-Pyrénées
exact_mappings:
- dpv_loc:FR-N
- dpv_loc_owl:FR-N
is_a: FR
class_uri: loc:FR-N

```
</details></div>