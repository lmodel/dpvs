---
search:
  boost: 10.0
---

# Class: GRI 


_Concept representing region Attica in country Greece_



<div data-search-exclude markdown="1">



URI: [loc:GR-I](https://w3id.org/lmodel/dpv/loc/GR-I)





```mermaid
 classDiagram
    class GRI
    click GRI href "../GRI/"
      GR <|-- GRI
        click GR href "../GR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [GR](GR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **GRI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GR-I](https://w3id.org/lmodel/dpv/loc/GR-I) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GR-I
* Attica




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GR-I |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GR-I |
| native | loc:GRI |
| exact | dpv_loc:GR-I, dpv_loc_owl:GR-I |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GRI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-I
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Attica in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-I
- Attica
exact_mappings:
- dpv_loc:GR-I
- dpv_loc_owl:GR-I
is_a: GR
class_uri: loc:GR-I

```
</details>

### Induced

<details>
```yaml
name: GRI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GR-I
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Attica in country Greece
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GR-I
- Attica
exact_mappings:
- dpv_loc:GR-I
- dpv_loc_owl:GR-I
is_a: GR
class_uri: loc:GR-I

```
</details></div>