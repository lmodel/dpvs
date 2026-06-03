---
search:
  boost: 10.0
---

# Class: CLBI 


_Concept representing region Biobío Region in country Chile_



<div data-search-exclude markdown="1">



URI: [loc:CL-BI](https://w3id.org/lmodel/dpv/loc/CL-BI)





```mermaid
 classDiagram
    class CLBI
    click CLBI href "../CLBI/"
      CL <|-- CLBI
        click CL href "../CL/"
      
      
```





## Inheritance
* [CL](CL.md)
    * **CLBI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CL-BI](https://w3id.org/lmodel/dpv/loc/CL-BI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CL-BI
* Biobío Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CL-BI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CL-BI |
| native | loc:CLBI |
| exact | dpv_loc:CL-BI, dpv_loc_owl:CL-BI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CLBI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CL-BI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Biobío Region in country Chile
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CL-BI
- Biobío Region
exact_mappings:
- dpv_loc:CL-BI
- dpv_loc_owl:CL-BI
is_a: CL
class_uri: loc:CL-BI

```
</details>

### Induced

<details>
```yaml
name: CLBI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CL-BI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Biobío Region in country Chile
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CL-BI
- Biobío Region
exact_mappings:
- dpv_loc:CL-BI
- dpv_loc_owl:CL-BI
is_a: CL
class_uri: loc:CL-BI

```
</details></div>