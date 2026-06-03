---
search:
  boost: 10.0
---

# Class: CLRM 


_Concept representing region Santiago Metropolitan Region in country_

_Chile_



<div data-search-exclude markdown="1">



URI: [loc:CL-RM](https://w3id.org/lmodel/dpv/loc/CL-RM)





```mermaid
 classDiagram
    class CLRM
    click CLRM href "../CLRM/"
      CL <|-- CLRM
        click CL href "../CL/"
      
      
```





## Inheritance
* [CL](CL.md)
    * **CLRM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CL-RM](https://w3id.org/lmodel/dpv/loc/CL-RM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CL-RM
* Santiago Metropolitan Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CL-RM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CL-RM |
| native | loc:CLRM |
| exact | dpv_loc:CL-RM, dpv_loc_owl:CL-RM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CLRM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CL-RM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Santiago Metropolitan Region in country

  Chile'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CL-RM
- Santiago Metropolitan Region
exact_mappings:
- dpv_loc:CL-RM
- dpv_loc_owl:CL-RM
is_a: CL
class_uri: loc:CL-RM

```
</details>

### Induced

<details>
```yaml
name: CLRM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CL-RM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Santiago Metropolitan Region in country

  Chile'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CL-RM
- Santiago Metropolitan Region
exact_mappings:
- dpv_loc:CL-RM
- dpv_loc_owl:CL-RM
is_a: CL
class_uri: loc:CL-RM

```
</details></div>