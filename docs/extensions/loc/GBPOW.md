---
search:
  boost: 10.0
---

# Class: GBPOW 


_Concept representing region Powys in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-POW](https://w3id.org/lmodel/dpv/loc/GB-POW)





```mermaid
 classDiagram
    class GBPOW
    click GBPOW href "../GBPOW/"
      GB <|-- GBPOW
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBPOW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-POW](https://w3id.org/lmodel/dpv/loc/GB-POW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-POW
* Powys




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-POW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-POW |
| native | loc:GBPOW |
| exact | dpv_loc:GB-POW, dpv_loc_owl:GB-POW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBPOW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-POW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Powys in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-POW
- Powys
exact_mappings:
- dpv_loc:GB-POW
- dpv_loc_owl:GB-POW
is_a: GB
class_uri: loc:GB-POW

```
</details>

### Induced

<details>
```yaml
name: GBPOW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-POW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Powys in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-POW
- Powys
exact_mappings:
- dpv_loc:GB-POW
- dpv_loc_owl:GB-POW
is_a: GB
class_uri: loc:GB-POW

```
</details></div>