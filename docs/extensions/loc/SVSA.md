---
search:
  boost: 10.0
---

# Class: SVSA 


_Concept representing region Santa Ana Department in country El Salvador_



<div data-search-exclude markdown="1">



URI: [loc:SV-SA](https://w3id.org/lmodel/dpv/loc/SV-SA)





```mermaid
 classDiagram
    class SVSA
    click SVSA href "../SVSA/"
      SV <|-- SVSA
        click SV href "../SV/"
      
      
```





## Inheritance
* [SV](SV.md)
    * **SVSA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SV-SA](https://w3id.org/lmodel/dpv/loc/SV-SA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SV-SA
* Santa Ana Department




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SV-SA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SV-SA |
| native | loc:SVSA |
| exact | dpv_loc:SV-SA, dpv_loc_owl:SV-SA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SVSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SV-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Santa Ana Department in country El Salvador
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SV-SA
- Santa Ana Department
exact_mappings:
- dpv_loc:SV-SA
- dpv_loc_owl:SV-SA
is_a: SV
class_uri: loc:SV-SA

```
</details>

### Induced

<details>
```yaml
name: SVSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SV-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Santa Ana Department in country El Salvador
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SV-SA
- Santa Ana Department
exact_mappings:
- dpv_loc:SV-SA
- dpv_loc_owl:SV-SA
is_a: SV
class_uri: loc:SV-SA

```
</details></div>