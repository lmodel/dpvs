---
search:
  boost: 10.0
---

# Class: ISASA 


_Concept representing region Ásahreppur in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-ASA](https://w3id.org/lmodel/dpv/loc/IS-ASA)





```mermaid
 classDiagram
    class ISASA
    click ISASA href "../ISASA/"
      IS <|-- ISASA
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISASA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-ASA](https://w3id.org/lmodel/dpv/loc/IS-ASA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-ASA
* Ásahreppur




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-ASA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-ASA |
| native | loc:ISASA |
| exact | dpv_loc:IS-ASA, dpv_loc_owl:IS-ASA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISASA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-ASA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ásahreppur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-ASA
- Ásahreppur
exact_mappings:
- dpv_loc:IS-ASA
- dpv_loc_owl:IS-ASA
is_a: IS
class_uri: loc:IS-ASA

```
</details>

### Induced

<details>
```yaml
name: ISASA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-ASA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ásahreppur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-ASA
- Ásahreppur
exact_mappings:
- dpv_loc:IS-ASA
- dpv_loc_owl:IS-ASA
is_a: IS
class_uri: loc:IS-ASA

```
</details></div>