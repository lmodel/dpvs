---
search:
  boost: 10.0
---

# Class: PGNCD 


_Concept representing region Port Moresby in country Papua New Guinea_



<div data-search-exclude markdown="1">



URI: [loc:PG-NCD](https://w3id.org/lmodel/dpv/loc/PG-NCD)





```mermaid
 classDiagram
    class PGNCD
    click PGNCD href "../PGNCD/"
      PG <|-- PGNCD
        click PG href "../PG/"
      
      
```





## Inheritance
* [PG](PG.md)
    * **PGNCD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PG-NCD](https://w3id.org/lmodel/dpv/loc/PG-NCD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* PG-NCD
* Port Moresby




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PG-NCD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PG-NCD |
| native | loc:PGNCD |
| exact | dpv_loc:PG-NCD, dpv_loc_owl:PG-NCD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PGNCD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PG-NCD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Port Moresby in country Papua New Guinea
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PG-NCD
- Port Moresby
exact_mappings:
- dpv_loc:PG-NCD
- dpv_loc_owl:PG-NCD
is_a: PG
class_uri: loc:PG-NCD

```
</details>

### Induced

<details>
```yaml
name: PGNCD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PG-NCD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Port Moresby in country Papua New Guinea
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PG-NCD
- Port Moresby
exact_mappings:
- dpv_loc:PG-NCD
- dpv_loc_owl:PG-NCD
is_a: PG
class_uri: loc:PG-NCD

```
</details></div>