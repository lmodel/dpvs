---
search:
  boost: 10.0
---

# Class: GBABC 


_Concept representing region Armagh, Banbridge and Craigavon in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-ABC](https://w3id.org/lmodel/dpv/loc/GB-ABC)





```mermaid
 classDiagram
    class GBABC
    click GBABC href "../GBABC/"
      GB <|-- GBABC
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBABC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-ABC](https://w3id.org/lmodel/dpv/loc/GB-ABC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-ABC
* Armagh, Banbridge and Craigavon




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-ABC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-ABC |
| native | loc:GBABC |
| exact | dpv_loc:GB-ABC, dpv_loc_owl:GB-ABC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBABC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ABC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Armagh, Banbridge and Craigavon in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ABC
- Armagh, Banbridge and Craigavon
exact_mappings:
- dpv_loc:GB-ABC
- dpv_loc_owl:GB-ABC
is_a: GB
class_uri: loc:GB-ABC

```
</details>

### Induced

<details>
```yaml
name: GBABC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-ABC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Armagh, Banbridge and Craigavon in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-ABC
- Armagh, Banbridge and Craigavon
exact_mappings:
- dpv_loc:GB-ABC
- dpv_loc_owl:GB-ABC
is_a: GB
class_uri: loc:GB-ABC

```
</details></div>