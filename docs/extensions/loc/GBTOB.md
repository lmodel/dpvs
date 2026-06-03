---
search:
  boost: 10.0
---

# Class: GBTOB 


_Concept representing region Borough of Torbay in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-TOB](https://w3id.org/lmodel/dpv/loc/GB-TOB)





```mermaid
 classDiagram
    class GBTOB
    click GBTOB href "../GBTOB/"
      GB <|-- GBTOB
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBTOB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-TOB](https://w3id.org/lmodel/dpv/loc/GB-TOB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-TOB
* Borough of Torbay




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-TOB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-TOB |
| native | loc:GBTOB |
| exact | dpv_loc:GB-TOB, dpv_loc_owl:GB-TOB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBTOB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-TOB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Torbay in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-TOB
- Borough of Torbay
exact_mappings:
- dpv_loc:GB-TOB
- dpv_loc_owl:GB-TOB
is_a: GB
class_uri: loc:GB-TOB

```
</details>

### Induced

<details>
```yaml
name: GBTOB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-TOB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Torbay in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-TOB
- Borough of Torbay
exact_mappings:
- dpv_loc:GB-TOB
- dpv_loc_owl:GB-TOB
is_a: GB
class_uri: loc:GB-TOB

```
</details></div>