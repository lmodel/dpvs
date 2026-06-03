---
search:
  boost: 10.0
---

# Class: TLLA 


_Concept representing region Lautém (Municipality) in country Timor-Leste_



<div data-search-exclude markdown="1">



URI: [loc:TL-LA](https://w3id.org/lmodel/dpv/loc/TL-LA)





```mermaid
 classDiagram
    class TLLA
    click TLLA href "../TLLA/"
      TL <|-- TLLA
        click TL href "../TL/"
      
      
```





## Inheritance
* [TL](TL.md)
    * **TLLA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:TL-LA](https://w3id.org/lmodel/dpv/loc/TL-LA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* TL-LA
* Lautém (Municipality)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#TL-LA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:TL-LA |
| native | loc:TLLA |
| exact | dpv_loc:TL-LA, dpv_loc_owl:TL-LA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TLLA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TL-LA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Lautém (Municipality) in country Timor-Leste
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TL-LA
- Lautém (Municipality)
exact_mappings:
- dpv_loc:TL-LA
- dpv_loc_owl:TL-LA
is_a: TL
class_uri: loc:TL-LA

```
</details>

### Induced

<details>
```yaml
name: TLLA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TL-LA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Lautém (Municipality) in country Timor-Leste
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TL-LA
- Lautém (Municipality)
exact_mappings:
- dpv_loc:TL-LA
- dpv_loc_owl:TL-LA
is_a: TL
class_uri: loc:TL-LA

```
</details></div>