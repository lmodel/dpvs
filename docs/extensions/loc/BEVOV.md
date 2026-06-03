---
search:
  boost: 10.0
---

# Class: BEVOV 


_Concept representing region East Flanders in country Belgium_



<div data-search-exclude markdown="1">



URI: [loc:BE-VOV](https://w3id.org/lmodel/dpv/loc/BE-VOV)





```mermaid
 classDiagram
    class BEVOV
    click BEVOV href "../BEVOV/"
      BE <|-- BEVOV
        click BE href "../BE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [BE](BE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **BEVOV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BE-VOV](https://w3id.org/lmodel/dpv/loc/BE-VOV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BE-VOV
* East Flanders




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BE-VOV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BE-VOV |
| native | loc:BEVOV |
| exact | dpv_loc:BE-VOV, dpv_loc_owl:BE-VOV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BEVOV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-VOV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region East Flanders in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-VOV
- East Flanders
exact_mappings:
- dpv_loc:BE-VOV
- dpv_loc_owl:BE-VOV
is_a: BE
class_uri: loc:BE-VOV

```
</details>

### Induced

<details>
```yaml
name: BEVOV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BE-VOV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region East Flanders in country Belgium
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BE-VOV
- East Flanders
exact_mappings:
- dpv_loc:BE-VOV
- dpv_loc_owl:BE-VOV
is_a: BE
class_uri: loc:BE-VOV

```
</details></div>