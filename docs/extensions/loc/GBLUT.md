---
search:
  boost: 10.0
---

# Class: GBLUT 


_Concept representing region Luton in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-LUT](https://w3id.org/lmodel/dpv/loc/GB-LUT)





```mermaid
 classDiagram
    class GBLUT
    click GBLUT href "../GBLUT/"
      GB <|-- GBLUT
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBLUT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-LUT](https://w3id.org/lmodel/dpv/loc/GB-LUT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-LUT
* Luton




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-LUT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-LUT |
| native | loc:GBLUT |
| exact | dpv_loc:GB-LUT, dpv_loc_owl:GB-LUT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBLUT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LUT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Luton in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LUT
- Luton
exact_mappings:
- dpv_loc:GB-LUT
- dpv_loc_owl:GB-LUT
is_a: GB
class_uri: loc:GB-LUT

```
</details>

### Induced

<details>
```yaml
name: GBLUT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LUT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Luton in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LUT
- Luton
exact_mappings:
- dpv_loc:GB-LUT
- dpv_loc_owl:GB-LUT
is_a: GB
class_uri: loc:GB-LUT

```
</details></div>