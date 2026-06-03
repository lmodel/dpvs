---
search:
  boost: 10.0
---

# Class: GBWND 


_Concept representing region London Borough of Wandsworth in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-WND](https://w3id.org/lmodel/dpv/loc/GB-WND)





```mermaid
 classDiagram
    class GBWND
    click GBWND href "../GBWND/"
      GB <|-- GBWND
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBWND**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-WND](https://w3id.org/lmodel/dpv/loc/GB-WND) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-WND
* London Borough of Wandsworth




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-WND |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-WND |
| native | loc:GBWND |
| exact | dpv_loc:GB-WND, dpv_loc_owl:GB-WND |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBWND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Wandsworth in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WND
- London Borough of Wandsworth
exact_mappings:
- dpv_loc:GB-WND
- dpv_loc_owl:GB-WND
is_a: GB
class_uri: loc:GB-WND

```
</details>

### Induced

<details>
```yaml
name: GBWND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Wandsworth in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WND
- London Borough of Wandsworth
exact_mappings:
- dpv_loc:GB-WND
- dpv_loc_owl:GB-WND
is_a: GB
class_uri: loc:GB-WND

```
</details></div>