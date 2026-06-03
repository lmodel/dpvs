---
search:
  boost: 10.0
---

# Class: PEHUC 


_Concept representing region Huánuco Region in country Peru_



<div data-search-exclude markdown="1">



URI: [loc:PE-HUC](https://w3id.org/lmodel/dpv/loc/PE-HUC)





```mermaid
 classDiagram
    class PEHUC
    click PEHUC href "../PEHUC/"
      PE <|-- PEHUC
        click PE href "../PE/"
      
      
```





## Inheritance
* [PE](PE.md)
    * **PEHUC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PE-HUC](https://w3id.org/lmodel/dpv/loc/PE-HUC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* PE-HUC
* Huánuco Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PE-HUC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PE-HUC |
| native | loc:PEHUC |
| exact | dpv_loc:PE-HUC, dpv_loc_owl:PE-HUC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PEHUC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PE-HUC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Huánuco Region in country Peru
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PE-HUC
- Huánuco Region
exact_mappings:
- dpv_loc:PE-HUC
- dpv_loc_owl:PE-HUC
is_a: PE
class_uri: loc:PE-HUC

```
</details>

### Induced

<details>
```yaml
name: PEHUC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PE-HUC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Huánuco Region in country Peru
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PE-HUC
- Huánuco Region
exact_mappings:
- dpv_loc:PE-HUC
- dpv_loc_owl:PE-HUC
is_a: PE
class_uri: loc:PE-HUC

```
</details></div>