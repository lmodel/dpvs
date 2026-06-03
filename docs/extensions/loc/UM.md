---
search:
  boost: 10.0
---

# Class: UM 


_Concept representing Country of United States Minor Outlying Islands_



<div data-search-exclude markdown="1">



URI: [loc:UM](https://w3id.org/lmodel/dpv/loc/UM)





```mermaid
 classDiagram
    class UM
    click UM href "../UM/"
      US <|-- UM
        click US href "../US/"
      

      UM <|-- UM67
        click UM67 href "../UM67/"
      UM <|-- UM71
        click UM71 href "../UM71/"
      UM <|-- UM76
        click UM76 href "../UM76/"
      UM <|-- UM79
        click UM79 href "../UM79/"
      UM <|-- UM81
        click UM81 href "../UM81/"
      UM <|-- UM84
        click UM84 href "../UM84/"
      UM <|-- UM86
        click UM86 href "../UM86/"
      UM <|-- UM89
        click UM89 href "../UM89/"
      UM <|-- UM95
        click UM95 href "../UM95/"
      

      
```





## Inheritance
* [US](US.md)
    * **UM**
        * [UM67](UM67.md)
        * [UM71](UM71.md)
        * [UM76](UM76.md)
        * [UM79](UM79.md)
        * [UM81](UM81.md)
        * [UM84](UM84.md)
        * [UM86](UM86.md)
        * [UM89](UM89.md)
        * [UM95](UM95.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:UM](https://w3id.org/lmodel/dpv/loc/UM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* United States Minor Outlying Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#UM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:UM |
| native | loc:UM |
| exact | dpv_loc:UM, dpv_loc_owl:UM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#UM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of United States Minor Outlying Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- United States Minor Outlying Islands
exact_mappings:
- dpv_loc:UM
- dpv_loc_owl:UM
is_a: US
class_uri: loc:UM

```
</details>

### Induced

<details>
```yaml
name: UM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#UM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of United States Minor Outlying Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- United States Minor Outlying Islands
exact_mappings:
- dpv_loc:UM
- dpv_loc_owl:UM
is_a: US
class_uri: loc:UM

```
</details></div>