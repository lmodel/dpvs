---
search:
  boost: 10.0
---

# Class: GBSCT 


_Concept representing region Scotland in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-SCT](https://w3id.org/lmodel/dpv/loc/GB-SCT)





```mermaid
 classDiagram
    class GBSCT
    click GBSCT href "../GBSCT/"
      GB <|-- GBSCT
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSCT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-SCT](https://w3id.org/lmodel/dpv/loc/GB-SCT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-SCT
* Scotland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-SCT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-SCT |
| native | loc:GBSCT |
| exact | dpv_loc:GB-SCT, dpv_loc_owl:GB-SCT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSCT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SCT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Scotland in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SCT
- Scotland
exact_mappings:
- dpv_loc:GB-SCT
- dpv_loc_owl:GB-SCT
is_a: GB
class_uri: loc:GB-SCT

```
</details>

### Induced

<details>
```yaml
name: GBSCT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SCT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Scotland in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SCT
- Scotland
exact_mappings:
- dpv_loc:GB-SCT
- dpv_loc_owl:GB-SCT
is_a: GB
class_uri: loc:GB-SCT

```
</details></div>