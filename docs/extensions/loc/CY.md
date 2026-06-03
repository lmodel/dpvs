---
search:
  boost: 10.0
---

# Class: CY 


_Concept representing Country of Cyprus_



<div data-search-exclude markdown="1">



URI: [loc:CY](https://w3id.org/lmodel/dpv/loc/CY)





```mermaid
 classDiagram
    class CY
    click CY href "../CY/"
      EEA30 <|-- CY
        click EEA30 href "../EEA30/"
      EEA31 <|-- CY
        click EEA31 href "../EEA31/"
      EU <|-- CY
        click EU href "../EU/"
      EU27 <|-- CY
        click EU27 href "../EU27/"
      EU28 <|-- CY
        click EU28 href "../EU28/"
      EEA <|-- CY
        click EEA href "../EEA/"
      

      CY <|-- CY01
        click CY01 href "../CY01/"
      CY <|-- CY02
        click CY02 href "../CY02/"
      CY <|-- CY03
        click CY03 href "../CY03/"
      CY <|-- CY04
        click CY04 href "../CY04/"
      CY <|-- CY05
        click CY05 href "../CY05/"
      CY <|-- CY06
        click CY06 href "../CY06/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **CY** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [CY01](CY01.md)
        * [CY02](CY02.md)
        * [CY03](CY03.md)
        * [CY04](CY04.md)
        * [CY05](CY05.md)
        * [CY06](CY06.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CY](https://w3id.org/lmodel/dpv/loc/CY) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Cyprus




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CY |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CY |
| native | loc:CY |
| exact | dpv_loc:CY, dpv_loc_owl:CY |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Cyprus
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Cyprus
exact_mappings:
- dpv_loc:CY
- dpv_loc_owl:CY
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:CY

```
</details>

### Induced

<details>
```yaml
name: CY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Cyprus
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Cyprus
exact_mappings:
- dpv_loc:CY
- dpv_loc_owl:CY
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:CY

```
</details></div>