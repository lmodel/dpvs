---
search:
  boost: 10.0
---

# Class: GBSLG 


_Concept representing region Borough of Slough in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-SLG](https://w3id.org/lmodel/dpv/loc/GB-SLG)





```mermaid
 classDiagram
    class GBSLG
    click GBSLG href "../GBSLG/"
      GB <|-- GBSLG
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSLG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-SLG](https://w3id.org/lmodel/dpv/loc/GB-SLG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-SLG
* Borough of Slough




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-SLG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-SLG |
| native | loc:GBSLG |
| exact | dpv_loc:GB-SLG, dpv_loc_owl:GB-SLG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSLG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SLG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Slough in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SLG
- Borough of Slough
exact_mappings:
- dpv_loc:GB-SLG
- dpv_loc_owl:GB-SLG
is_a: GB
class_uri: loc:GB-SLG

```
</details>

### Induced

<details>
```yaml
name: GBSLG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SLG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Slough in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SLG
- Borough of Slough
exact_mappings:
- dpv_loc:GB-SLG
- dpv_loc_owl:GB-SLG
is_a: GB
class_uri: loc:GB-SLG

```
</details></div>