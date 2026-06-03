---
search:
  boost: 10.0
---

# Class: GBNBL 


_Concept representing region Northumberland in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-NBL](https://w3id.org/lmodel/dpv/loc/GB-NBL)





```mermaid
 classDiagram
    class GBNBL
    click GBNBL href "../GBNBL/"
      GB <|-- GBNBL
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBNBL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-NBL](https://w3id.org/lmodel/dpv/loc/GB-NBL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-NBL
* Northumberland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-NBL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-NBL |
| native | loc:GBNBL |
| exact | dpv_loc:GB-NBL, dpv_loc_owl:GB-NBL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBNBL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NBL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Northumberland in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NBL
- Northumberland
exact_mappings:
- dpv_loc:GB-NBL
- dpv_loc_owl:GB-NBL
is_a: GB
class_uri: loc:GB-NBL

```
</details>

### Induced

<details>
```yaml
name: GBNBL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NBL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Northumberland in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NBL
- Northumberland
exact_mappings:
- dpv_loc:GB-NBL
- dpv_loc_owl:GB-NBL
is_a: GB
class_uri: loc:GB-NBL

```
</details></div>