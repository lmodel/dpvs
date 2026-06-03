---
search:
  boost: 10.0
---

# Class: GBABE 


_Concept representing region Aberdeen in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ABE](https://w3id.org/lmodel/dpv/loc/GB-ABE)





```mermaid
 classDiagram
    class GBABE
    click GBABE href "../GBABE/"
      GB <|-- GBABE
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBABE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ABE](https://w3id.org/lmodel/dpv/loc/GB-ABE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ABE
* Aberdeen




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ABE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ABE |
| native | loc:GBABE |
| exact | dpv_loc:GB-ABE, dpv_loc_owl:GB-ABE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBABE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ABE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Aberdeen in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ABE
- Aberdeen
exact_mappings:
- dpv_loc:GB-ABE
- dpv_loc_owl:GB-ABE
is_a: GB
class_uri: loc:GB-ABE

```
</details>

### Induced

<details>
```yaml
name: GBABE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ABE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Aberdeen in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ABE
- Aberdeen
exact_mappings:
- dpv_loc:GB-ABE
- dpv_loc_owl:GB-ABE
is_a: GB
class_uri: loc:GB-ABE

```
</details></div>