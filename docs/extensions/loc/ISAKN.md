---
search:
  boost: 10.0
---

# Class: ISAKN 


_Concept representing region Akranes in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-AKN](https://w3id.org/lmodel/dpv/loc/IS-AKN)





```mermaid
 classDiagram
    class ISAKN
    click ISAKN href "../ISAKN/"
      IS <|-- ISAKN
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISAKN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-AKN](https://w3id.org/lmodel/dpv/loc/IS-AKN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-AKN
* Akranes




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-AKN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-AKN |
| native | loc:ISAKN |
| exact | dpv_loc:IS-AKN, dpv_loc_owl:IS-AKN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISAKN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-AKN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Akranes in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-AKN
- Akranes
exact_mappings:
- dpv_loc:IS-AKN
- dpv_loc_owl:IS-AKN
is_a: IS
class_uri: loc:IS-AKN

```
</details>

### Induced

<details>
```yaml
name: ISAKN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-AKN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Akranes in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-AKN
- Akranes
exact_mappings:
- dpv_loc:IS-AKN
- dpv_loc_owl:IS-AKN
is_a: IS
class_uri: loc:IS-AKN

```
</details></div>