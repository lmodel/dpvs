---
search:
  boost: 10.0
---

# Class: TLLI 


_Concept representing region Liquiçá (Municipality) in country_

_Timor-Leste_



<div data-search-exclude markdown="1">



URI: [loc:TL-LI](https://w3id.org/lmodel/dpv/loc/TL-LI)





```mermaid
 classDiagram
    class TLLI
    click TLLI href "../TLLI/"
      TL <|-- TLLI
        click TL href "../TL/"
      
      
```





## Inheritance
* [TL](TL.md)
    * **TLLI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:TL-LI](https://w3id.org/lmodel/dpv/loc/TL-LI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* TL-LI
* Liquiçá (Municipality)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#TL-LI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:TL-LI |
| native | loc:TLLI |
| exact | dpv_loc:TL-LI, dpv_loc_owl:TL-LI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TLLI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TL-LI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Liquiçá (Municipality) in country

  Timor-Leste'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TL-LI
- Liquiçá (Municipality)
exact_mappings:
- dpv_loc:TL-LI
- dpv_loc_owl:TL-LI
is_a: TL
class_uri: loc:TL-LI

```
</details>

### Induced

<details>
```yaml
name: TLLI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TL-LI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Liquiçá (Municipality) in country

  Timor-Leste'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TL-LI
- Liquiçá (Municipality)
exact_mappings:
- dpv_loc:TL-LI
- dpv_loc_owl:TL-LI
is_a: TL
class_uri: loc:TL-LI

```
</details></div>