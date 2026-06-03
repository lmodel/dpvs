---
search:
  boost: 10.0
---

# Class: GBGLG 


_Concept representing region Glasgow in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-GLG](https://w3id.org/lmodel/dpv/loc/GB-GLG)





```mermaid
 classDiagram
    class GBGLG
    click GBGLG href "../GBGLG/"
      GB <|-- GBGLG
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBGLG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-GLG](https://w3id.org/lmodel/dpv/loc/GB-GLG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-GLG
* Glasgow




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-GLG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-GLG |
| native | loc:GBGLG |
| exact | dpv_loc:GB-GLG, dpv_loc_owl:GB-GLG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBGLG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-GLG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Glasgow in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-GLG
- Glasgow
exact_mappings:
- dpv_loc:GB-GLG
- dpv_loc_owl:GB-GLG
is_a: GB
class_uri: loc:GB-GLG

```
</details>

### Induced

<details>
```yaml
name: GBGLG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-GLG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Glasgow in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-GLG
- Glasgow
exact_mappings:
- dpv_loc:GB-GLG
- dpv_loc_owl:GB-GLG
is_a: GB
class_uri: loc:GB-GLG

```
</details></div>