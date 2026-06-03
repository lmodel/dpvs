---
search:
  boost: 10.0
---

# Class: TWKIN 


_Concept representing region Kinmen in country Taiwan (Province of China)_



<div data-search-exclude markdown="1">



URI: [loc:TW-KIN](https://w3id.org/lmodel/dpv/loc/TW-KIN)





```mermaid
 classDiagram
    class TWKIN
    click TWKIN href "../TWKIN/"
      TW <|-- TWKIN
        click TW href "../TW/"
      
      
```





## Inheritance
* [TW](TW.md)
    * **TWKIN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:TW-KIN](https://w3id.org/lmodel/dpv/loc/TW-KIN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* TW-KIN
* Kinmen




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#TW-KIN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:TW-KIN |
| native | loc:TWKIN |
| exact | dpv_loc:TW-KIN, dpv_loc_owl:TW-KIN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TWKIN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TW-KIN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kinmen in country Taiwan (Province of China)
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TW-KIN
- Kinmen
exact_mappings:
- dpv_loc:TW-KIN
- dpv_loc_owl:TW-KIN
is_a: TW
class_uri: loc:TW-KIN

```
</details>

### Induced

<details>
```yaml
name: TWKIN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#TW-KIN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kinmen in country Taiwan (Province of China)
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- TW-KIN
- Kinmen
exact_mappings:
- dpv_loc:TW-KIN
- dpv_loc_owl:TW-KIN
is_a: TW
class_uri: loc:TW-KIN

```
</details></div>