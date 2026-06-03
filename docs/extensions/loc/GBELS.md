---
search:
  boost: 10.0
---

# Class: GBELS 


_Concept representing region Outer Hebrides in country United Kingdom of_

_Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ELS](https://w3id.org/lmodel/dpv/loc/GB-ELS)





```mermaid
 classDiagram
    class GBELS
    click GBELS href "../GBELS/"
      GB <|-- GBELS
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBELS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ELS](https://w3id.org/lmodel/dpv/loc/GB-ELS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ELS
* Outer Hebrides




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ELS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ELS |
| native | loc:GBELS |
| exact | dpv_loc:GB-ELS, dpv_loc_owl:GB-ELS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBELS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ELS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Outer Hebrides in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ELS
- Outer Hebrides
exact_mappings:
- dpv_loc:GB-ELS
- dpv_loc_owl:GB-ELS
is_a: GB
class_uri: loc:GB-ELS

```
</details>

### Induced

<details>
```yaml
name: GBELS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ELS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Outer Hebrides in country United Kingdom
  of

  Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ELS
- Outer Hebrides
exact_mappings:
- dpv_loc:GB-ELS
- dpv_loc_owl:GB-ELS
is_a: GB
class_uri: loc:GB-ELS

```
</details></div>