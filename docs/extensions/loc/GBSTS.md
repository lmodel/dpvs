---
search:
  boost: 10.0
---

# Class: GBSTS 


_Concept representing region Staffordshire in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-STS](https://w3id.org/lmodel/dpv/loc/GB-STS)





```mermaid
 classDiagram
    class GBSTS
    click GBSTS href "../GBSTS/"
      GB <|-- GBSTS
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSTS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-STS](https://w3id.org/lmodel/dpv/loc/GB-STS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-STS
* Staffordshire




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-STS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-STS |
| native | loc:GBSTS |
| exact | dpv_loc:GB-STS, dpv_loc_owl:GB-STS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSTS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-STS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Staffordshire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-STS
- Staffordshire
exact_mappings:
- dpv_loc:GB-STS
- dpv_loc_owl:GB-STS
is_a: GB
class_uri: loc:GB-STS

```
</details>

### Induced

<details>
```yaml
name: GBSTS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-STS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Staffordshire in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-STS
- Staffordshire
exact_mappings:
- dpv_loc:GB-STS
- dpv_loc_owl:GB-STS
is_a: GB
class_uri: loc:GB-STS

```
</details></div>