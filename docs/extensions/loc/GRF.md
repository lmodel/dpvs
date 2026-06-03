---
search:
  boost: 10.0
---

# Class: GRF 


_Concept representing region Ionian Islands in country Greece_



<div data-search-exclude markdown="1">



URI: [loc:GR-F](https://w3id.org/lmodel/dpv/loc/GR-F)





```mermaid
 classDiagram
    class GRF
    click GRF href "../GRF/"
      GR <|-- GRF
        click GR href "../GR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [GR](GR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **GRF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GR-F](https://w3id.org/lmodel/dpv/loc/GR-F) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GR-F
* Ionian Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GR-F |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GR-F |
| native | loc:GRF |
| exact | dpv_loc:GR-F, dpv_loc_owl:GR-F |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GRF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-F
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ionian Islands in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-F
- Ionian Islands
exact_mappings:
- dpv_loc:GR-F
- dpv_loc_owl:GR-F
is_a: GR
class_uri: loc:GR-F

```
</details>

### Induced

<details>
```yaml
name: GRF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-F
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ionian Islands in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-F
- Ionian Islands
exact_mappings:
- dpv_loc:GR-F
- dpv_loc_owl:GR-F
is_a: GR
class_uri: loc:GR-F

```
</details></div>