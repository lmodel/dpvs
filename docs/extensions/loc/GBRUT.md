---
search:
  boost: 10.0
---

# Class: GBRUT 


_Concept representing region Rutland in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-RUT](https://w3id.org/lmodel/dpv/loc/GB-RUT)





```mermaid
 classDiagram
    class GBRUT
    click GBRUT href "../GBRUT/"
      GB <|-- GBRUT
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBRUT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-RUT](https://w3id.org/lmodel/dpv/loc/GB-RUT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-RUT
* Rutland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-RUT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-RUT |
| native | loc:GBRUT |
| exact | dpv_loc:GB-RUT, dpv_loc_owl:GB-RUT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBRUT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-RUT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Rutland in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-RUT
- Rutland
exact_mappings:
- dpv_loc:GB-RUT
- dpv_loc_owl:GB-RUT
is_a: GB
class_uri: loc:GB-RUT

```
</details>

### Induced

<details>
```yaml
name: GBRUT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-RUT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Rutland in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-RUT
- Rutland
exact_mappings:
- dpv_loc:GB-RUT
- dpv_loc_owl:GB-RUT
is_a: GB
class_uri: loc:GB-RUT

```
</details></div>