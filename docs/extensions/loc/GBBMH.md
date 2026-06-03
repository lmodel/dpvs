---
search:
  boost: 10.0
---

# Class: GBBMH 


_Concept representing region Borough of Bournemouth in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-BMH](https://w3id.org/lmodel/dpv/loc/GB-BMH)





```mermaid
 classDiagram
    class GBBMH
    click GBBMH href "../GBBMH/"
      GB <|-- GBBMH
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBBMH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-BMH](https://w3id.org/lmodel/dpv/loc/GB-BMH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-BMH
* Borough of Bournemouth




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-BMH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-BMH |
| native | loc:GBBMH |
| exact | dpv_loc:GB-BMH, dpv_loc_owl:GB-BMH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBBMH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BMH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Bournemouth in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BMH
- Borough of Bournemouth
exact_mappings:
- dpv_loc:GB-BMH
- dpv_loc_owl:GB-BMH
is_a: GB
class_uri: loc:GB-BMH

```
</details>

### Induced

<details>
```yaml
name: GBBMH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BMH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Bournemouth in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BMH
- Borough of Bournemouth
exact_mappings:
- dpv_loc:GB-BMH
- dpv_loc_owl:GB-BMH
is_a: GB
class_uri: loc:GB-BMH

```
</details></div>