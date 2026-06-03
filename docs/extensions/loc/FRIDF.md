---
search:
  boost: 10.0
---

# Class: FRIDF 


_Concept representing region Île-de-France in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-IDF](https://w3id.org/lmodel/dpv/loc/FR-IDF)





```mermaid
 classDiagram
    class FRIDF
    click FRIDF href "../FRIDF/"
      FR <|-- FRIDF
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRIDF**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-IDF](https://w3id.org/lmodel/dpv/loc/FR-IDF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-IDF
* Île-de-France




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-IDF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-IDF |
| native | loc:FRIDF |
| exact | dpv_loc:FR-IDF, dpv_loc_owl:FR-IDF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRIDF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-IDF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Île-de-France in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-IDF
- Île-de-France
exact_mappings:
- dpv_loc:FR-IDF
- dpv_loc_owl:FR-IDF
is_a: FR
class_uri: loc:FR-IDF

```
</details>

### Induced

<details>
```yaml
name: FRIDF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-IDF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Île-de-France in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-IDF
- Île-de-France
exact_mappings:
- dpv_loc:FR-IDF
- dpv_loc_owl:FR-IDF
is_a: FR
class_uri: loc:FR-IDF

```
</details></div>