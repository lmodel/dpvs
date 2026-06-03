---
search:
  boost: 10.0
---

# Class: ISKOP 


_Concept representing region Kópavogur (city) in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-KOP](https://w3id.org/lmodel/dpv/loc/IS-KOP)





```mermaid
 classDiagram
    class ISKOP
    click ISKOP href "../ISKOP/"
      IS <|-- ISKOP
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISKOP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-KOP](https://w3id.org/lmodel/dpv/loc/IS-KOP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-KOP
* Kópavogur (city)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-KOP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-KOP |
| native | loc:ISKOP |
| exact | dpv_loc:IS-KOP, dpv_loc_owl:IS-KOP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISKOP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-KOP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kópavogur (city) in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-KOP
- Kópavogur (city)
exact_mappings:
- dpv_loc:IS-KOP
- dpv_loc_owl:IS-KOP
is_a: IS
class_uri: loc:IS-KOP

```
</details>

### Induced

<details>
```yaml
name: ISKOP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-KOP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Kópavogur (city) in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-KOP
- Kópavogur (city)
exact_mappings:
- dpv_loc:IS-KOP
- dpv_loc_owl:IS-KOP
is_a: IS
class_uri: loc:IS-KOP

```
</details></div>