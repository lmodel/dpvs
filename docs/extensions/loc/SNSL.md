---
search:
  boost: 10.0
---

# Class: SNSL 


_Concept representing region Saint-Louis Region in country Senegal_



<div data-search-exclude markdown="1">



URI: [loc:SN-SL](https://w3id.org/lmodel/dpv/loc/SN-SL)





```mermaid
 classDiagram
    class SNSL
    click SNSL href "../SNSL/"
      SN <|-- SNSL
        click SN href "../SN/"
      
      
```





## Inheritance
* [SN](SN.md)
    * **SNSL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SN-SL](https://w3id.org/lmodel/dpv/loc/SN-SL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SN-SL
* Saint-Louis Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SN-SL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SN-SL |
| native | loc:SNSL |
| exact | dpv_loc:SN-SL, dpv_loc_owl:SN-SL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SNSL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SN-SL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saint-Louis Region in country Senegal
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SN-SL
- Saint-Louis Region
exact_mappings:
- dpv_loc:SN-SL
- dpv_loc_owl:SN-SL
is_a: SN
class_uri: loc:SN-SL

```
</details>

### Induced

<details>
```yaml
name: SNSL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SN-SL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saint-Louis Region in country Senegal
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SN-SL
- Saint-Louis Region
exact_mappings:
- dpv_loc:SN-SL
- dpv_loc_owl:SN-SL
is_a: SN
class_uri: loc:SN-SL

```
</details></div>