---
search:
  boost: 10.0
---

# Class: VNDN 


_Concept representing region Da Nang in country Viet Nam_



<div data-search-exclude markdown="1">



URI: [loc:VN-DN](https://w3id.org/lmodel/dpv/loc/VN-DN)





```mermaid
 classDiagram
    class VNDN
    click VNDN href "../VNDN/"
      VN <|-- VNDN
        click VN href "../VN/"
      
      
```





## Inheritance
* [VN](VN.md)
    * **VNDN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:VN-DN](https://w3id.org/lmodel/dpv/loc/VN-DN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* VN-DN
* Da Nang




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#VN-DN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:VN-DN |
| native | loc:VNDN |
| exact | dpv_loc:VN-DN, dpv_loc_owl:VN-DN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VNDN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VN-DN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Da Nang in country Viet Nam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VN-DN
- Da Nang
exact_mappings:
- dpv_loc:VN-DN
- dpv_loc_owl:VN-DN
is_a: VN
class_uri: loc:VN-DN

```
</details>

### Induced

<details>
```yaml
name: VNDN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VN-DN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Da Nang in country Viet Nam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VN-DN
- Da Nang
exact_mappings:
- dpv_loc:VN-DN
- dpv_loc_owl:VN-DN
is_a: VN
class_uri: loc:VN-DN

```
</details></div>