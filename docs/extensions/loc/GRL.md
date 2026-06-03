---
search:
  boost: 10.0
---

# Class: GRL 


_Concept representing region South Aegean in country Greece_



<div data-search-exclude markdown="1">



URI: [loc:GR-L](https://w3id.org/lmodel/dpv/loc/GR-L)





```mermaid
 classDiagram
    class GRL
    click GRL href "../GRL/"
      GR <|-- GRL
        click GR href "../GR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [GR](GR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **GRL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GR-L](https://w3id.org/lmodel/dpv/loc/GR-L) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GR-L
* South Aegean




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GR-L |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GR-L |
| native | loc:GRL |
| exact | dpv_loc:GR-L, dpv_loc_owl:GR-L |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GRL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region South Aegean in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-L
- South Aegean
exact_mappings:
- dpv_loc:GR-L
- dpv_loc_owl:GR-L
is_a: GR
class_uri: loc:GR-L

```
</details>

### Induced

<details>
```yaml
name: GRL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-L
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region South Aegean in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-L
- South Aegean
exact_mappings:
- dpv_loc:GR-L
- dpv_loc_owl:GR-L
is_a: GR
class_uri: loc:GR-L

```
</details></div>