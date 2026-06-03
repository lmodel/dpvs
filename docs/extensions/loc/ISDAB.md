---
search:
  boost: 10.0
---

# Class: ISDAB 


_Concept representing region Dalabyggð in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-DAB](https://w3id.org/lmodel/dpv/loc/IS-DAB)





```mermaid
 classDiagram
    class ISDAB
    click ISDAB href "../ISDAB/"
      IS <|-- ISDAB
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISDAB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-DAB](https://w3id.org/lmodel/dpv/loc/IS-DAB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-DAB
* Dalabyggð




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-DAB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-DAB |
| native | loc:ISDAB |
| exact | dpv_loc:IS-DAB, dpv_loc_owl:IS-DAB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISDAB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-DAB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dalabyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-DAB
- Dalabyggð
exact_mappings:
- dpv_loc:IS-DAB
- dpv_loc_owl:IS-DAB
is_a: IS
class_uri: loc:IS-DAB

```
</details>

### Induced

<details>
```yaml
name: ISDAB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-DAB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dalabyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-DAB
- Dalabyggð
exact_mappings:
- dpv_loc:IS-DAB
- dpv_loc_owl:IS-DAB
is_a: IS
class_uri: loc:IS-DAB

```
</details></div>