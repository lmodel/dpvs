---
search:
  boost: 10.0
---

# Class: GBEDH 


_Concept representing region Edinburgh in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-EDH](https://w3id.org/lmodel/dpv/loc/GB-EDH)





```mermaid
 classDiagram
    class GBEDH
    click GBEDH href "../GBEDH/"
      GB <|-- GBEDH
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBEDH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-EDH](https://w3id.org/lmodel/dpv/loc/GB-EDH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-EDH
* Edinburgh




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-EDH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-EDH |
| native | loc:GBEDH |
| exact | dpv_loc:GB-EDH, dpv_loc_owl:GB-EDH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBEDH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-EDH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Edinburgh in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-EDH
- Edinburgh
exact_mappings:
- dpv_loc:GB-EDH
- dpv_loc_owl:GB-EDH
is_a: GB
class_uri: loc:GB-EDH

```
</details>

### Induced

<details>
```yaml
name: GBEDH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-EDH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Edinburgh in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-EDH
- Edinburgh
exact_mappings:
- dpv_loc:GB-EDH
- dpv_loc_owl:GB-EDH
is_a: GB
class_uri: loc:GB-EDH

```
</details></div>