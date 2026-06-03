---
search:
  boost: 10.0
---

# Class: GBMDW 


_Concept representing region Borough of Medway in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-MDW](https://w3id.org/lmodel/dpv/loc/GB-MDW)





```mermaid
 classDiagram
    class GBMDW
    click GBMDW href "../GBMDW/"
      GB <|-- GBMDW
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBMDW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-MDW](https://w3id.org/lmodel/dpv/loc/GB-MDW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-MDW
* Borough of Medway




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-MDW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-MDW |
| native | loc:GBMDW |
| exact | dpv_loc:GB-MDW, dpv_loc_owl:GB-MDW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBMDW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MDW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Medway in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MDW
- Borough of Medway
exact_mappings:
- dpv_loc:GB-MDW
- dpv_loc_owl:GB-MDW
is_a: GB
class_uri: loc:GB-MDW

```
</details>

### Induced

<details>
```yaml
name: GBMDW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MDW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Medway in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MDW
- Borough of Medway
exact_mappings:
- dpv_loc:GB-MDW
- dpv_loc_owl:GB-MDW
is_a: GB
class_uri: loc:GB-MDW

```
</details></div>