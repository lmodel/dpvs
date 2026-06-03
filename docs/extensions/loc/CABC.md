---
search:
  boost: 10.0
---

# Class: CABC 


_Concept representing region British Columbia in country Canada_



<div data-search-exclude markdown="1">



URI: [loc:CA-BC](https://w3id.org/lmodel/dpv/loc/CA-BC)





```mermaid
 classDiagram
    class CABC
    click CABC href "../CABC/"
      CA <|-- CABC
        click CA href "../CA/"
      
      
```





## Inheritance
* [CA](CA.md)
    * **CABC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CA-BC](https://w3id.org/lmodel/dpv/loc/CA-BC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CA-BC
* British Columbia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CA-BC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CA-BC |
| native | loc:CABC |
| exact | dpv_loc:CA-BC, dpv_loc_owl:CA-BC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CABC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CA-BC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region British Columbia in country Canada
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CA-BC
- British Columbia
exact_mappings:
- dpv_loc:CA-BC
- dpv_loc_owl:CA-BC
is_a: CA
class_uri: loc:CA-BC

```
</details>

### Induced

<details>
```yaml
name: CABC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CA-BC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region British Columbia in country Canada
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CA-BC
- British Columbia
exact_mappings:
- dpv_loc:CA-BC
- dpv_loc_owl:CA-BC
is_a: CA
class_uri: loc:CA-BC

```
</details></div>