---
search:
  boost: 10.0
---

# Class: GRD 


_Concept representing region Epirus (region) in country Greece_



<div data-search-exclude markdown="1">



URI: [loc:GR-D](https://w3id.org/lmodel/dpv/loc/GR-D)





```mermaid
 classDiagram
    class GRD
    click GRD href "../GRD/"
      GR <|-- GRD
        click GR href "../GR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [GR](GR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **GRD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GR-D](https://w3id.org/lmodel/dpv/loc/GR-D) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GR-D
* Epirus (region)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GR-D |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GR-D |
| native | loc:GRD |
| exact | dpv_loc:GR-D, dpv_loc_owl:GR-D |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GRD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-D
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Epirus (region) in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-D
- Epirus (region)
exact_mappings:
- dpv_loc:GR-D
- dpv_loc_owl:GR-D
is_a: GR
class_uri: loc:GR-D

```
</details>

### Induced

<details>
```yaml
name: GRD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-D
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Epirus (region) in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-D
- Epirus (region)
exact_mappings:
- dpv_loc:GR-D
- dpv_loc_owl:GR-D
is_a: GR
class_uri: loc:GR-D

```
</details></div>