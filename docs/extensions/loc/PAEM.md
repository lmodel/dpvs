---
search:
  boost: 10.0
---

# Class: PAEM 


_Concept representing region Embera in country Panama_



<div data-search-exclude markdown="1">



URI: [loc:PA-EM](https://w3id.org/lmodel/dpv/loc/PA-EM)





```mermaid
 classDiagram
    class PAEM
    click PAEM href "../PAEM/"
      PA <|-- PAEM
        click PA href "../PA/"
      
      
```





## Inheritance
* [PA](PA.md)
    * **PAEM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PA-EM](https://w3id.org/lmodel/dpv/loc/PA-EM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* PA-EM
* Embera




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PA-EM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PA-EM |
| native | loc:PAEM |
| exact | dpv_loc:PA-EM, dpv_loc_owl:PA-EM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PAEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PA-EM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Embera in country Panama
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PA-EM
- Embera
exact_mappings:
- dpv_loc:PA-EM
- dpv_loc_owl:PA-EM
is_a: PA
class_uri: loc:PA-EM

```
</details>

### Induced

<details>
```yaml
name: PAEM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PA-EM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Embera in country Panama
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PA-EM
- Embera
exact_mappings:
- dpv_loc:PA-EM
- dpv_loc_owl:PA-EM
is_a: PA
class_uri: loc:PA-EM

```
</details></div>