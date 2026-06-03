---
search:
  boost: 10.0
---

# Class: CAON 


_Concept representing region Ontario in country Canada_



<div data-search-exclude markdown="1">



URI: [loc:CA-ON](https://w3id.org/lmodel/dpv/loc/CA-ON)





```mermaid
 classDiagram
    class CAON
    click CAON href "../CAON/"
      CA <|-- CAON
        click CA href "../CA/"
      
      
```





## Inheritance
* [CA](CA.md)
    * **CAON**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CA-ON](https://w3id.org/lmodel/dpv/loc/CA-ON) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CA-ON
* Ontario




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CA-ON |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CA-ON |
| native | loc:CAON |
| exact | dpv_loc:CA-ON, dpv_loc_owl:CA-ON |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CAON
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CA-ON
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ontario in country Canada
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CA-ON
- Ontario
exact_mappings:
- dpv_loc:CA-ON
- dpv_loc_owl:CA-ON
is_a: CA
class_uri: loc:CA-ON

```
</details>

### Induced

<details>
```yaml
name: CAON
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CA-ON
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ontario in country Canada
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CA-ON
- Ontario
exact_mappings:
- dpv_loc:CA-ON
- dpv_loc_owl:CA-ON
is_a: CA
class_uri: loc:CA-ON

```
</details></div>