---
search:
  boost: 10.0
---

# Class: GBCGN 


_Concept representing region Ceredigion in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-CGN](https://w3id.org/lmodel/dpv/loc/GB-CGN)





```mermaid
 classDiagram
    class GBCGN
    click GBCGN href "../GBCGN/"
      GB <|-- GBCGN
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBCGN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-CGN](https://w3id.org/lmodel/dpv/loc/GB-CGN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-CGN
* Ceredigion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-CGN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-CGN |
| native | loc:GBCGN |
| exact | dpv_loc:GB-CGN, dpv_loc_owl:GB-CGN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBCGN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-CGN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Ceredigion in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-CGN
- Ceredigion
exact_mappings:
- dpv_loc:GB-CGN
- dpv_loc_owl:GB-CGN
is_a: GB
class_uri: loc:GB-CGN

```
</details>

### Induced

<details>
```yaml
name: GBCGN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-CGN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Ceredigion in country United Kingdom of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-CGN
- Ceredigion
exact_mappings:
- dpv_loc:GB-CGN
- dpv_loc_owl:GB-CGN
is_a: GB
class_uri: loc:GB-CGN

```
</details></div>