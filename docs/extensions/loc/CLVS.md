---
search:
  boost: 10.0
---

# Class: CLVS 


_Concept representing region Valparaíso Region in country Chile_



<div data-search-exclude markdown="1">



URI: [loc:CL-VS](https://w3id.org/lmodel/dpv/loc/CL-VS)





```mermaid
 classDiagram
    class CLVS
    click CLVS href "../CLVS/"
      CL <|-- CLVS
        click CL href "../CL/"
      
      
```





## Inheritance
* [CL](CL.md)
    * **CLVS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CL-VS](https://w3id.org/lmodel/dpv/loc/CL-VS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CL-VS
* Valparaíso Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CL-VS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CL-VS |
| native | loc:CLVS |
| exact | dpv_loc:CL-VS, dpv_loc_owl:CL-VS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CLVS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CL-VS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Valparaíso Region in country Chile
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CL-VS
- Valparaíso Region
exact_mappings:
- dpv_loc:CL-VS
- dpv_loc_owl:CL-VS
is_a: CL
class_uri: loc:CL-VS

```
</details>

### Induced

<details>
```yaml
name: CLVS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CL-VS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Valparaíso Region in country Chile
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CL-VS
- Valparaíso Region
exact_mappings:
- dpv_loc:CL-VS
- dpv_loc_owl:CL-VS
is_a: CL
class_uri: loc:CL-VS

```
</details></div>