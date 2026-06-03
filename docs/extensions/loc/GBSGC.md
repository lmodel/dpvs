---
search:
  boost: 10.0
---

# Class: GBSGC 


_Concept representing region South Gloucestershire District in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-SGC](https://w3id.org/lmodel/dpv/loc/GB-SGC)





```mermaid
 classDiagram
    class GBSGC
    click GBSGC href "../GBSGC/"
      GB <|-- GBSGC
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSGC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-SGC](https://w3id.org/lmodel/dpv/loc/GB-SGC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-SGC
* South Gloucestershire District




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-SGC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-SGC |
| native | loc:GBSGC |
| exact | dpv_loc:GB-SGC, dpv_loc_owl:GB-SGC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSGC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SGC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region South Gloucestershire District in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SGC
- South Gloucestershire District
exact_mappings:
- dpv_loc:GB-SGC
- dpv_loc_owl:GB-SGC
is_a: GB
class_uri: loc:GB-SGC

```
</details>

### Induced

<details>
```yaml
name: GBSGC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SGC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region South Gloucestershire District in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SGC
- South Gloucestershire District
exact_mappings:
- dpv_loc:GB-SGC
- dpv_loc_owl:GB-SGC
is_a: GB
class_uri: loc:GB-SGC

```
</details></div>