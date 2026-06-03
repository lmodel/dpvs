---
search:
  boost: 10.0
---

# Class: GBWLS 


_Concept representing region Wales in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-WLS](https://w3id.org/lmodel/dpv/loc/GB-WLS)





```mermaid
 classDiagram
    class GBWLS
    click GBWLS href "../GBWLS/"
      GB <|-- GBWLS
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBWLS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-WLS](https://w3id.org/lmodel/dpv/loc/GB-WLS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-WLS
* Wales




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-WLS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-WLS |
| native | loc:GBWLS |
| exact | dpv_loc:GB-WLS, dpv_loc_owl:GB-WLS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBWLS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WLS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Wales in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WLS
- Wales
exact_mappings:
- dpv_loc:GB-WLS
- dpv_loc_owl:GB-WLS
is_a: GB
class_uri: loc:GB-WLS

```
</details>

### Induced

<details>
```yaml
name: GBWLS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WLS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Wales in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WLS
- Wales
exact_mappings:
- dpv_loc:GB-WLS
- dpv_loc_owl:GB-WLS
is_a: GB
class_uri: loc:GB-WLS

```
</details></div>