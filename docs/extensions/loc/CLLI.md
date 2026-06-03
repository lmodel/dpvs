---
search:
  boost: 10.0
---

# Class: CLLI 


_Concept representing region O'Higgins Region in country Chile_



<div data-search-exclude markdown="1">



URI: [loc:CL-LI](https://w3id.org/lmodel/dpv/loc/CL-LI)





```mermaid
 classDiagram
    class CLLI
    click CLLI href "../CLLI/"
      CL <|-- CLLI
        click CL href "../CL/"
      
      
```





## Inheritance
* [CL](CL.md)
    * **CLLI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CL-LI](https://w3id.org/lmodel/dpv/loc/CL-LI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CL-LI
* O'Higgins Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CL-LI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CL-LI |
| native | loc:CLLI |
| exact | dpv_loc:CL-LI, dpv_loc_owl:CL-LI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CLLI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CL-LI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region O'Higgins Region in country Chile
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CL-LI
- O'Higgins Region
exact_mappings:
- dpv_loc:CL-LI
- dpv_loc_owl:CL-LI
is_a: CL
class_uri: loc:CL-LI

```
</details>

### Induced

<details>
```yaml
name: CLLI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CL-LI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region O'Higgins Region in country Chile
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CL-LI
- O'Higgins Region
exact_mappings:
- dpv_loc:CL-LI
- dpv_loc_owl:CL-LI
is_a: CL
class_uri: loc:CL-LI

```
</details></div>