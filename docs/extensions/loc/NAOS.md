---
search:
  boost: 10.0
---

# Class: NAOS 


_Concept representing region Omusati in country Namibia_



<div data-search-exclude markdown="1">



URI: [loc:NA-OS](https://w3id.org/lmodel/dpv/loc/NA-OS)





```mermaid
 classDiagram
    class NAOS
    click NAOS href "../NAOS/"
      NA <|-- NAOS
        click NA href "../NA/"
      
      
```





## Inheritance
* [NA](NA.md)
    * **NAOS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NA-OS](https://w3id.org/lmodel/dpv/loc/NA-OS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NA-OS
* Omusati




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NA-OS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NA-OS |
| native | loc:NAOS |
| exact | dpv_loc:NA-OS, dpv_loc_owl:NA-OS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NAOS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NA-OS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Omusati in country Namibia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NA-OS
- Omusati
exact_mappings:
- dpv_loc:NA-OS
- dpv_loc_owl:NA-OS
is_a: NA
class_uri: loc:NA-OS

```
</details>

### Induced

<details>
```yaml
name: NAOS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NA-OS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Omusati in country Namibia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NA-OS
- Omusati
exact_mappings:
- dpv_loc:NA-OS
- dpv_loc_owl:NA-OS
is_a: NA
class_uri: loc:NA-OS

```
</details></div>