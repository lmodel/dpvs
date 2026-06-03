---
search:
  boost: 10.0
---

# Class: GRC 


_Concept representing region West Macedonia in country Greece_



<div data-search-exclude markdown="1">



URI: [loc:GR-C](https://w3id.org/lmodel/dpv/loc/GR-C)





```mermaid
 classDiagram
    class GRC
    click GRC href "../GRC/"
      GR <|-- GRC
        click GR href "../GR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [GR](GR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **GRC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GR-C](https://w3id.org/lmodel/dpv/loc/GR-C) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GR-C
* West Macedonia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GR-C |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GR-C |
| native | loc:GRC |
| exact | dpv_loc:GR-C, dpv_loc_owl:GR-C |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GRC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region West Macedonia in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-C
- West Macedonia
exact_mappings:
- dpv_loc:GR-C
- dpv_loc_owl:GR-C
is_a: GR
class_uri: loc:GR-C

```
</details>

### Induced

<details>
```yaml
name: GRC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region West Macedonia in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-C
- West Macedonia
exact_mappings:
- dpv_loc:GR-C
- dpv_loc_owl:GR-C
is_a: GR
class_uri: loc:GR-C

```
</details></div>