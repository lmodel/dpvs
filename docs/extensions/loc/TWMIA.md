---
search:
  boost: 10.0
---

# Class: TWMIA 


_Concept representing region Miaoli County in country Taiwan (Province of_

_China)_



<div data-search-exclude markdown="1">



URI: [loc:TW-MIA](https://w3id.org/lmodel/dpv/loc/TW-MIA)





```mermaid
 classDiagram
    class TWMIA
    click TWMIA href "../TWMIA/"
      TW <|-- TWMIA
        click TW href "../TW/"
      
      
```





## Inheritance
* [TW](TW.md)
    * **TWMIA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:TW-MIA](https://w3id.org/lmodel/dpv/loc/TW-MIA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* TW-MIA
* Miaoli County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#TW-MIA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:TW-MIA |
| native | loc:TWMIA |
| exact | dpv_loc:TW-MIA, dpv_loc_owl:TW-MIA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TWMIA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TW-MIA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Miaoli County in country Taiwan (Province
  of

  China)'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TW-MIA
- Miaoli County
exact_mappings:
- dpv_loc:TW-MIA
- dpv_loc_owl:TW-MIA
is_a: TW
class_uri: loc:TW-MIA

```
</details>

### Induced

<details>
```yaml
name: TWMIA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TW-MIA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Miaoli County in country Taiwan (Province
  of

  China)'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TW-MIA
- Miaoli County
exact_mappings:
- dpv_loc:TW-MIA
- dpv_loc_owl:TW-MIA
is_a: TW
class_uri: loc:TW-MIA

```
</details></div>