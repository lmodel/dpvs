---
search:
  boost: 10.0
---

# Class: SZ 


_Concept representing Country of Eswatini_



<div data-search-exclude markdown="1">



URI: [loc:SZ](https://w3id.org/lmodel/dpv/loc/SZ)





```mermaid
 classDiagram
    class SZ
    click SZ href "../SZ/"
      SZ <|-- SZHH
        click SZHH href "../SZHH/"
      SZ <|-- SZLU
        click SZLU href "../SZLU/"
      SZ <|-- SZMA
        click SZMA href "../SZMA/"
      SZ <|-- SZSH
        click SZSH href "../SZSH/"
      
      
```





## Inheritance
* **SZ**
    * [SZHH](SZHH.md)
    * [SZLU](SZLU.md)
    * [SZMA](SZMA.md)
    * [SZSH](SZSH.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SZ](https://w3id.org/lmodel/dpv/loc/SZ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Eswatini




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SZ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SZ |
| native | loc:SZ |
| exact | dpv_loc:SZ, dpv_loc_owl:SZ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SZ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Eswatini
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Eswatini
exact_mappings:
- dpv_loc:SZ
- dpv_loc_owl:SZ
class_uri: loc:SZ

```
</details>

### Induced

<details>
```yaml
name: SZ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SZ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Eswatini
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Eswatini
exact_mappings:
- dpv_loc:SZ
- dpv_loc_owl:SZ
class_uri: loc:SZ

```
</details></div>