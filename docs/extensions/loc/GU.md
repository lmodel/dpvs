---
search:
  boost: 10.0
---

# Class: GU 


_Concept representing Country of Guam_



<div data-search-exclude markdown="1">



URI: [loc:GU](https://w3id.org/lmodel/dpv/loc/GU)





```mermaid
 classDiagram
    class GU
    click GU href "../GU/"
      US <|-- GU
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **GU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GU](https://w3id.org/lmodel/dpv/loc/GU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Guam




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GU |
| native | loc:GU |
| exact | dpv_loc:GU, dpv_loc_owl:GU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Guam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Guam
exact_mappings:
- dpv_loc:GU
- dpv_loc_owl:GU
is_a: US
class_uri: loc:GU

```
</details>

### Induced

<details>
```yaml
name: GU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Guam
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Guam
exact_mappings:
- dpv_loc:GU
- dpv_loc_owl:GU
is_a: US
class_uri: loc:GU

```
</details></div>