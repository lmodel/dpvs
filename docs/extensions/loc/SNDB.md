---
search:
  boost: 10.0
---

# Class: SNDB 


_Concept representing region Diourbel Region in country Senegal_



<div data-search-exclude markdown="1">



URI: [loc:SN-DB](https://w3id.org/lmodel/dpv/loc/SN-DB)





```mermaid
 classDiagram
    class SNDB
    click SNDB href "../SNDB/"
      SN <|-- SNDB
        click SN href "../SN/"
      
      
```





## Inheritance
* [SN](SN.md)
    * **SNDB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SN-DB](https://w3id.org/lmodel/dpv/loc/SN-DB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SN-DB
* Diourbel Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SN-DB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SN-DB |
| native | loc:SNDB |
| exact | dpv_loc:SN-DB, dpv_loc_owl:SN-DB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SNDB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SN-DB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Diourbel Region in country Senegal
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SN-DB
- Diourbel Region
exact_mappings:
- dpv_loc:SN-DB
- dpv_loc_owl:SN-DB
is_a: SN
class_uri: loc:SN-DB

```
</details>

### Induced

<details>
```yaml
name: SNDB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SN-DB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Diourbel Region in country Senegal
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SN-DB
- Diourbel Region
exact_mappings:
- dpv_loc:SN-DB
- dpv_loc_owl:SN-DB
is_a: SN
class_uri: loc:SN-DB

```
</details></div>