---
search:
  boost: 10.0
---

# Class: SH 


_Concept representing Country of Saint Helena_



<div data-search-exclude markdown="1">



URI: [loc:SH](https://w3id.org/lmodel/dpv/loc/SH)





```mermaid
 classDiagram
    class SH
    click SH href "../SH/"
      SH <|-- SHAC
        click SHAC href "../SHAC/"
      SH <|-- SHHL
        click SHHL href "../SHHL/"
      SH <|-- SHTA
        click SHTA href "../SHTA/"
      
      
```





## Inheritance
* **SH**
    * [SHAC](SHAC.md)
    * [SHHL](SHHL.md)
    * [SHTA](SHTA.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SH](https://w3id.org/lmodel/dpv/loc/SH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Saint Helena




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SH |
| native | loc:SH |
| exact | dpv_loc:SH, dpv_loc_owl:SH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Saint Helena
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Saint Helena
exact_mappings:
- dpv_loc:SH
- dpv_loc_owl:SH
class_uri: loc:SH

```
</details>

### Induced

<details>
```yaml
name: SH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Saint Helena
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Saint Helena
exact_mappings:
- dpv_loc:SH
- dpv_loc_owl:SH
class_uri: loc:SH

```
</details></div>