---
search:
  boost: 10.0
---

# Class: GBPEM 


_Concept representing region Pembrokeshire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-PEM](https://w3id.org/lmodel/dpv/loc/GB-PEM)





```mermaid
 classDiagram
    class GBPEM
    click GBPEM href "../GBPEM/"
      GB <|-- GBPEM
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBPEM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-PEM](https://w3id.org/lmodel/dpv/loc/GB-PEM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-PEM
* Pembrokeshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-PEM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-PEM |
| native | loc:GBPEM |
| exact | dpv_loc:GB-PEM, dpv_loc_owl:GB-PEM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBPEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-PEM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Pembrokeshire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-PEM
- Pembrokeshire
exact_mappings:
- dpv_loc:GB-PEM
- dpv_loc_owl:GB-PEM
is_a: GB
class_uri: loc:GB-PEM

```
</details>

### Induced

<details>
```yaml
name: GBPEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-PEM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Pembrokeshire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-PEM
- Pembrokeshire
exact_mappings:
- dpv_loc:GB-PEM
- dpv_loc_owl:GB-PEM
is_a: GB
class_uri: loc:GB-PEM

```
</details></div>