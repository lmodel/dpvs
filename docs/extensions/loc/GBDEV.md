---
search:
  boost: 10.0
---

# Class: GBDEV 


_Concept representing region Devon in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-DEV](https://w3id.org/lmodel/dpv/loc/GB-DEV)





```mermaid
 classDiagram
    class GBDEV
    click GBDEV href "../GBDEV/"
      GB <|-- GBDEV
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBDEV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-DEV](https://w3id.org/lmodel/dpv/loc/GB-DEV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-DEV
* Devon




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-DEV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-DEV |
| native | loc:GBDEV |
| exact | dpv_loc:GB-DEV, dpv_loc_owl:GB-DEV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBDEV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DEV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Devon in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DEV
- Devon
exact_mappings:
- dpv_loc:GB-DEV
- dpv_loc_owl:GB-DEV
is_a: GB
class_uri: loc:GB-DEV

```
</details>

### Induced

<details>
```yaml
name: GBDEV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DEV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Devon in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DEV
- Devon
exact_mappings:
- dpv_loc:GB-DEV
- dpv_loc_owl:GB-DEV
is_a: GB
class_uri: loc:GB-DEV

```
</details></div>