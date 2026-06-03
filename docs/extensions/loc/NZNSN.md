---
search:
  boost: 10.0
---

# Class: NZNSN 


_Concept representing region Nelson Region in country New Zealand_



<div data-search-exclude markdown="1">



URI: [loc:NZ-NSN](https://w3id.org/lmodel/dpv/loc/NZ-NSN)





```mermaid
 classDiagram
    class NZNSN
    click NZNSN href "../NZNSN/"
      NZ <|-- NZNSN
        click NZ href "../NZ/"
      
      
```





## Inheritance
* [NZ](NZ.md)
    * **NZNSN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NZ-NSN](https://w3id.org/lmodel/dpv/loc/NZ-NSN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NZ-NSN
* Nelson Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NZ-NSN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NZ-NSN |
| native | loc:NZNSN |
| exact | dpv_loc:NZ-NSN, dpv_loc_owl:NZ-NSN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NZNSN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-NSN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nelson Region in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-NSN
- Nelson Region
exact_mappings:
- dpv_loc:NZ-NSN
- dpv_loc_owl:NZ-NSN
is_a: NZ
class_uri: loc:NZ-NSN

```
</details>

### Induced

<details>
```yaml
name: NZNSN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-NSN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nelson Region in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-NSN
- Nelson Region
exact_mappings:
- dpv_loc:NZ-NSN
- dpv_loc_owl:NZ-NSN
is_a: NZ
class_uri: loc:NZ-NSN

```
</details></div>