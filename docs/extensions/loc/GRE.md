---
search:
  boost: 10.0
---

# Class: GRE 


_Concept representing region Thessalia in country Greece_



<div data-search-exclude markdown="1">



URI: [loc:GR-E](https://w3id.org/lmodel/dpv/loc/GR-E)





```mermaid
 classDiagram
    class GRE
    click GRE href "../GRE/"
      GR <|-- GRE
        click GR href "../GR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [GR](GR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **GRE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GR-E](https://w3id.org/lmodel/dpv/loc/GR-E) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GR-E
* Thessalia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GR-E |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GR-E |
| native | loc:GRE |
| exact | dpv_loc:GR-E, dpv_loc_owl:GR-E |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GRE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-E
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Thessalia in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-E
- Thessalia
exact_mappings:
- dpv_loc:GR-E
- dpv_loc_owl:GR-E
is_a: GR
class_uri: loc:GR-E

```
</details>

### Induced

<details>
```yaml
name: GRE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-E
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Thessalia in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-E
- Thessalia
exact_mappings:
- dpv_loc:GR-E
- dpv_loc_owl:GR-E
is_a: GR
class_uri: loc:GR-E

```
</details></div>