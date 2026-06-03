---
search:
  boost: 10.0
---

# Class: MW 


_Concept representing Country of Malawi_



<div data-search-exclude markdown="1">



URI: [loc:MW](https://w3id.org/lmodel/dpv/loc/MW)





```mermaid
 classDiagram
    class MW
    click MW href "../MW/"
      MW <|-- MWKS
        click MWKS href "../MWKS/"
      MW <|-- MWMG
        click MWMG href "../MWMG/"
      MW <|-- MWMH
        click MWMH href "../MWMH/"
      MW <|-- MWMZ
        click MWMZ href "../MWMZ/"
      MW <|-- MWNB
        click MWNB href "../MWNB/"
      MW <|-- MWPH
        click MWPH href "../MWPH/"
      MW <|-- MWRU
        click MWRU href "../MWRU/"
      MW <|-- MWSA
        click MWSA href "../MWSA/"
      
      
```





## Inheritance
* **MW**
    * [MWKS](MWKS.md)
    * [MWMG](MWMG.md)
    * [MWMH](MWMH.md)
    * [MWMZ](MWMZ.md)
    * [MWNB](MWNB.md)
    * [MWPH](MWPH.md)
    * [MWRU](MWRU.md)
    * [MWSA](MWSA.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MW](https://w3id.org/lmodel/dpv/loc/MW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Malawi




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MW |
| native | loc:MW |
| exact | dpv_loc:MW, dpv_loc_owl:MW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Malawi
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Malawi
exact_mappings:
- dpv_loc:MW
- dpv_loc_owl:MW
class_uri: loc:MW

```
</details>

### Induced

<details>
```yaml
name: MW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Malawi
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Malawi
exact_mappings:
- dpv_loc:MW
- dpv_loc_owl:MW
class_uri: loc:MW

```
</details></div>