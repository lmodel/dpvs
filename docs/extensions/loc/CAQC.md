---
search:
  boost: 10.0
---

# Class: CAQC 


_Concept representing region Quebec in country Canada_



<div data-search-exclude markdown="1">



URI: [loc:CA-QC](https://w3id.org/lmodel/dpv/loc/CA-QC)





```mermaid
 classDiagram
    class CAQC
    click CAQC href "../CAQC/"
      CA <|-- CAQC
        click CA href "../CA/"
      
      
```





## Inheritance
* [CA](CA.md)
    * **CAQC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CA-QC](https://w3id.org/lmodel/dpv/loc/CA-QC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CA-QC
* Quebec




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CA-QC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CA-QC |
| native | loc:CAQC |
| exact | dpv_loc:CA-QC, dpv_loc_owl:CA-QC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CAQC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CA-QC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Quebec in country Canada
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CA-QC
- Quebec
exact_mappings:
- dpv_loc:CA-QC
- dpv_loc_owl:CA-QC
is_a: CA
class_uri: loc:CA-QC

```
</details>

### Induced

<details>
```yaml
name: CAQC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CA-QC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Quebec in country Canada
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CA-QC
- Quebec
exact_mappings:
- dpv_loc:CA-QC
- dpv_loc_owl:CA-QC
is_a: CA
class_uri: loc:CA-QC

```
</details></div>