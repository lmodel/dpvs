---
search:
  boost: 10.0
---

# Class: MCMO 


_Concept representing region Monaco-Ville in country Monaco_



<div data-search-exclude markdown="1">



URI: [loc:MC-MO](https://w3id.org/lmodel/dpv/loc/MC-MO)





```mermaid
 classDiagram
    class MCMO
    click MCMO href "../MCMO/"
      MC <|-- MCMO
        click MC href "../MC/"
      
      
```





## Inheritance
* [MC](MC.md)
    * **MCMO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MC-MO](https://w3id.org/lmodel/dpv/loc/MC-MO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* MC-MO
* Monaco-Ville




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MC-MO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MC-MO |
| native | loc:MCMO |
| exact | dpv_loc:MC-MO, dpv_loc_owl:MC-MO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MCMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MC-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Monaco-Ville in country Monaco
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MC-MO
- Monaco-Ville
exact_mappings:
- dpv_loc:MC-MO
- dpv_loc_owl:MC-MO
is_a: MC
class_uri: loc:MC-MO

```
</details>

### Induced

<details>
```yaml
name: MCMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MC-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Monaco-Ville in country Monaco
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MC-MO
- Monaco-Ville
exact_mappings:
- dpv_loc:MC-MO
- dpv_loc_owl:MC-MO
is_a: MC
class_uri: loc:MC-MO

```
</details></div>