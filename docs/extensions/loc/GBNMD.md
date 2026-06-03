---
search:
  boost: 10.0
---

# Class: GBNMD 


_Concept representing region Newry, Mourne and Down in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-NMD](https://w3id.org/lmodel/dpv/loc/GB-NMD)





```mermaid
 classDiagram
    class GBNMD
    click GBNMD href "../GBNMD/"
      GB <|-- GBNMD
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBNMD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-NMD](https://w3id.org/lmodel/dpv/loc/GB-NMD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-NMD
* Newry, Mourne and Down




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-NMD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-NMD |
| native | loc:GBNMD |
| exact | dpv_loc:GB-NMD, dpv_loc_owl:GB-NMD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBNMD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NMD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Newry, Mourne and Down in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NMD
- Newry, Mourne and Down
exact_mappings:
- dpv_loc:GB-NMD
- dpv_loc_owl:GB-NMD
is_a: GB
class_uri: loc:GB-NMD

```
</details>

### Induced

<details>
```yaml
name: GBNMD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NMD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Newry, Mourne and Down in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NMD
- Newry, Mourne and Down
exact_mappings:
- dpv_loc:GB-NMD
- dpv_loc_owl:GB-NMD
is_a: GB
class_uri: loc:GB-NMD

```
</details></div>