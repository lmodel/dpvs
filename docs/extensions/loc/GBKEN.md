---
search:
  boost: 10.0
---

# Class: GBKEN 


_Concept representing region Kent in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-KEN](https://w3id.org/lmodel/dpv/loc/GB-KEN)





```mermaid
 classDiagram
    class GBKEN
    click GBKEN href "../GBKEN/"
      GB <|-- GBKEN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBKEN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-KEN](https://w3id.org/lmodel/dpv/loc/GB-KEN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-KEN
* Kent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-KEN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-KEN |
| native | loc:GBKEN |
| exact | dpv_loc:GB-KEN, dpv_loc_owl:GB-KEN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBKEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-KEN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Kent in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-KEN
- Kent
exact_mappings:
- dpv_loc:GB-KEN
- dpv_loc_owl:GB-KEN
is_a: GB
class_uri: loc:GB-KEN

```
</details>

### Induced

<details>
```yaml
name: GBKEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-KEN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Kent in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-KEN
- Kent
exact_mappings:
- dpv_loc:GB-KEN
- dpv_loc_owl:GB-KEN
is_a: GB
class_uri: loc:GB-KEN

```
</details></div>