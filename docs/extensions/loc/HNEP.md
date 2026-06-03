---
search:
  boost: 10.0
---

# Class: HNEP 


_Concept representing region El Paraíso Department in country Honduras_



<div data-search-exclude markdown="1">



URI: [loc:HN-EP](https://w3id.org/lmodel/dpv/loc/HN-EP)





```mermaid
 classDiagram
    class HNEP
    click HNEP href "../HNEP/"
      HN <|-- HNEP
        click HN href "../HN/"
      
      
```





## Inheritance
* [HN](HN.md)
    * **HNEP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HN-EP](https://w3id.org/lmodel/dpv/loc/HN-EP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* HN-EP
* El Paraíso Department




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HN-EP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HN-EP |
| native | loc:HNEP |
| exact | dpv_loc:HN-EP, dpv_loc_owl:HN-EP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HNEP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HN-EP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region El Paraíso Department in country Honduras
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HN-EP
- El Paraíso Department
exact_mappings:
- dpv_loc:HN-EP
- dpv_loc_owl:HN-EP
is_a: HN
class_uri: loc:HN-EP

```
</details>

### Induced

<details>
```yaml
name: HNEP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HN-EP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region El Paraíso Department in country Honduras
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- HN-EP
- El Paraíso Department
exact_mappings:
- dpv_loc:HN-EP
- dpv_loc_owl:HN-EP
is_a: HN
class_uri: loc:HN-EP

```
</details></div>