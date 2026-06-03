---
search:
  boost: 10.0
---

# Class: SOSA 


_Concept representing region Sanaag Region (Somaliland) in country_

_Somalia_



<div data-search-exclude markdown="1">



URI: [loc:SO-SA](https://w3id.org/lmodel/dpv/loc/SO-SA)





```mermaid
 classDiagram
    class SOSA
    click SOSA href "../SOSA/"
      SO <|-- SOSA
        click SO href "../SO/"
      
      
```





## Inheritance
* [SO](SO.md)
    * **SOSA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SO-SA](https://w3id.org/lmodel/dpv/loc/SO-SA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SO-SA
* Sanaag Region (Somaliland)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SO-SA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SO-SA |
| native | loc:SOSA |
| exact | dpv_loc:SO-SA, dpv_loc_owl:SO-SA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SOSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SO-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Sanaag Region (Somaliland) in country

  Somalia'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SO-SA
- Sanaag Region (Somaliland)
exact_mappings:
- dpv_loc:SO-SA
- dpv_loc_owl:SO-SA
is_a: SO
class_uri: loc:SO-SA

```
</details>

### Induced

<details>
```yaml
name: SOSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SO-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Sanaag Region (Somaliland) in country

  Somalia'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SO-SA
- Sanaag Region (Somaliland)
exact_mappings:
- dpv_loc:SO-SA
- dpv_loc_owl:SO-SA
is_a: SO
class_uri: loc:SO-SA

```
</details></div>