---
search:
  boost: 10.0
---

# Class: GBANN 


_Concept representing region Antrim and Newtownabbey in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ANN](https://w3id.org/lmodel/dpv/loc/GB-ANN)





```mermaid
 classDiagram
    class GBANN
    click GBANN href "../GBANN/"
      GB <|-- GBANN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBANN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ANN](https://w3id.org/lmodel/dpv/loc/GB-ANN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ANN
* Antrim and Newtownabbey




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ANN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ANN |
| native | loc:GBANN |
| exact | dpv_loc:GB-ANN, dpv_loc_owl:GB-ANN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBANN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ANN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Antrim and Newtownabbey in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ANN
- Antrim and Newtownabbey
exact_mappings:
- dpv_loc:GB-ANN
- dpv_loc_owl:GB-ANN
is_a: GB
class_uri: loc:GB-ANN

```
</details>

### Induced

<details>
```yaml
name: GBANN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ANN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Antrim and Newtownabbey in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ANN
- Antrim and Newtownabbey
exact_mappings:
- dpv_loc:GB-ANN
- dpv_loc_owl:GB-ANN
is_a: GB
class_uri: loc:GB-ANN

```
</details></div>