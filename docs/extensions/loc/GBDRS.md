---
search:
  boost: 10.0
---

# Class: GBDRS 


_Concept representing region Derry and Strabane in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-DRS](https://w3id.org/lmodel/dpv/loc/GB-DRS)





```mermaid
 classDiagram
    class GBDRS
    click GBDRS href "../GBDRS/"
      GB <|-- GBDRS
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBDRS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-DRS](https://w3id.org/lmodel/dpv/loc/GB-DRS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-DRS
* Derry and Strabane




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-DRS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-DRS |
| native | loc:GBDRS |
| exact | dpv_loc:GB-DRS, dpv_loc_owl:GB-DRS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBDRS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DRS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Derry and Strabane in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DRS
- Derry and Strabane
exact_mappings:
- dpv_loc:GB-DRS
- dpv_loc_owl:GB-DRS
is_a: GB
class_uri: loc:GB-DRS

```
</details>

### Induced

<details>
```yaml
name: GBDRS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DRS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Derry and Strabane in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DRS
- Derry and Strabane
exact_mappings:
- dpv_loc:GB-DRS
- dpv_loc_owl:GB-DRS
is_a: GB
class_uri: loc:GB-DRS

```
</details></div>