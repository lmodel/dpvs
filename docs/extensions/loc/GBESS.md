---
search:
  boost: 10.0
---

# Class: GBESS 


_Concept representing region Essex in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ESS](https://w3id.org/lmodel/dpv/loc/GB-ESS)





```mermaid
 classDiagram
    class GBESS
    click GBESS href "../GBESS/"
      GB <|-- GBESS
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBESS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ESS](https://w3id.org/lmodel/dpv/loc/GB-ESS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ESS
* Essex




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ESS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ESS |
| native | loc:GBESS |
| exact | dpv_loc:GB-ESS, dpv_loc_owl:GB-ESS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBESS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ESS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Essex in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ESS
- Essex
exact_mappings:
- dpv_loc:GB-ESS
- dpv_loc_owl:GB-ESS
is_a: GB
class_uri: loc:GB-ESS

```
</details>

### Induced

<details>
```yaml
name: GBESS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ESS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Essex in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ESS
- Essex
exact_mappings:
- dpv_loc:GB-ESS
- dpv_loc_owl:GB-ESS
is_a: GB
class_uri: loc:GB-ESS

```
</details></div>