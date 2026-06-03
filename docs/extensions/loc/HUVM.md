---
search:
  boost: 10.0
---

# Class: HUVM 


_Concept representing region Veszprém in country Hungary_



<div data-search-exclude markdown="1">



URI: [loc:HU-VM](https://w3id.org/lmodel/dpv/loc/HU-VM)





```mermaid
 classDiagram
    class HUVM
    click HUVM href "../HUVM/"
      HU <|-- HUVM
        click HU href "../HU/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [HU](HU.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **HUVM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HU-VM](https://w3id.org/lmodel/dpv/loc/HU-VM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HU-VM
* Veszprém




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HU-VM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HU-VM |
| native | loc:HUVM |
| exact | dpv_loc:HU-VM, dpv_loc_owl:HU-VM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HUVM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-VM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Veszprém in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-VM
- Veszprém
exact_mappings:
- dpv_loc:HU-VM
- dpv_loc_owl:HU-VM
is_a: HU
class_uri: loc:HU-VM

```
</details>

### Induced

<details>
```yaml
name: HUVM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HU-VM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Veszprém in country Hungary
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HU-VM
- Veszprém
exact_mappings:
- dpv_loc:HU-VM
- dpv_loc_owl:HU-VM
is_a: HU
class_uri: loc:HU-VM

```
</details></div>