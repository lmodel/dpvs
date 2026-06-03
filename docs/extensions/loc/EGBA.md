---
search:
  boost: 10.0
---

# Class: EGBA 


_Concept representing region Red Sea Governorate in country Egypt_



<div data-search-exclude markdown="1">



URI: [loc:EG-BA](https://w3id.org/lmodel/dpv/loc/EG-BA)





```mermaid
 classDiagram
    class EGBA
    click EGBA href "../EGBA/"
      EG <|-- EGBA
        click EG href "../EG/"
      
      
```





## Inheritance
* [EG](EG.md)
    * **EGBA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:EG-BA](https://w3id.org/lmodel/dpv/loc/EG-BA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* EG-BA
* Red Sea Governorate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#EG-BA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:EG-BA |
| native | loc:EGBA |
| exact | dpv_loc:EG-BA, dpv_loc_owl:EG-BA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EGBA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-BA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Red Sea Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-BA
- Red Sea Governorate
exact_mappings:
- dpv_loc:EG-BA
- dpv_loc_owl:EG-BA
is_a: EG
class_uri: loc:EG-BA

```
</details>

### Induced

<details>
```yaml
name: EGBA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-BA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Red Sea Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-BA
- Red Sea Governorate
exact_mappings:
- dpv_loc:EG-BA
- dpv_loc_owl:EG-BA
is_a: EG
class_uri: loc:EG-BA

```
</details></div>