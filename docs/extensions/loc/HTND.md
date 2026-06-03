---
search:
  boost: 10.0
---

# Class: HTND 


_Concept representing region Nord (Haitian department) in country Haiti_



<div data-search-exclude markdown="1">



URI: [loc:HT-ND](https://w3id.org/lmodel/dpv/loc/HT-ND)





```mermaid
 classDiagram
    class HTND
    click HTND href "../HTND/"
      HT <|-- HTND
        click HT href "../HT/"
      
      
```





## Inheritance
* [HT](HT.md)
    * **HTND**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HT-ND](https://w3id.org/lmodel/dpv/loc/HT-ND) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HT-ND
* Nord (Haitian department)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HT-ND |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HT-ND |
| native | loc:HTND |
| exact | dpv_loc:HT-ND, dpv_loc_owl:HT-ND |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HTND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HT-ND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nord (Haitian department) in country Haiti
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HT-ND
- Nord (Haitian department)
exact_mappings:
- dpv_loc:HT-ND
- dpv_loc_owl:HT-ND
is_a: HT
class_uri: loc:HT-ND

```
</details>

### Induced

<details>
```yaml
name: HTND
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HT-ND
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nord (Haitian department) in country Haiti
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HT-ND
- Nord (Haitian department)
exact_mappings:
- dpv_loc:HT-ND
- dpv_loc_owl:HT-ND
is_a: HT
class_uri: loc:HT-ND

```
</details></div>