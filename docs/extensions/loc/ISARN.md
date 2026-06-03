---
search:
  boost: 10.0
---

# Class: ISARN 


_Concept representing region Árneshreppur in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-ARN](https://w3id.org/lmodel/dpv/loc/IS-ARN)





```mermaid
 classDiagram
    class ISARN
    click ISARN href "../ISARN/"
      IS <|-- ISARN
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISARN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-ARN](https://w3id.org/lmodel/dpv/loc/IS-ARN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-ARN
* Árneshreppur




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-ARN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-ARN |
| native | loc:ISARN |
| exact | dpv_loc:IS-ARN, dpv_loc_owl:IS-ARN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISARN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-ARN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Árneshreppur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-ARN
- Árneshreppur
exact_mappings:
- dpv_loc:IS-ARN
- dpv_loc_owl:IS-ARN
is_a: IS
class_uri: loc:IS-ARN

```
</details>

### Induced

<details>
```yaml
name: ISARN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-ARN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Árneshreppur in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-ARN
- Árneshreppur
exact_mappings:
- dpv_loc:IS-ARN
- dpv_loc_owl:IS-ARN
is_a: IS
class_uri: loc:IS-ARN

```
</details></div>