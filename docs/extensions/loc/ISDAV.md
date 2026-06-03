---
search:
  boost: 10.0
---

# Class: ISDAV 


_Concept representing region Dalvíkurbyggð in country Iceland_



<div data-search-exclude markdown="1">



URI: [loc:IS-DAV](https://w3id.org/lmodel/dpv/loc/IS-DAV)





```mermaid
 classDiagram
    class ISDAV
    click ISDAV href "../ISDAV/"
      IS <|-- ISDAV
        click IS href "../IS/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IS](IS.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **ISDAV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IS-DAV](https://w3id.org/lmodel/dpv/loc/IS-DAV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IS-DAV
* Dalvíkurbyggð




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IS-DAV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IS-DAV |
| native | loc:ISDAV |
| exact | dpv_loc:IS-DAV, dpv_loc_owl:IS-DAV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISDAV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-DAV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dalvíkurbyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-DAV
- Dalvíkurbyggð
exact_mappings:
- dpv_loc:IS-DAV
- dpv_loc_owl:IS-DAV
is_a: IS
class_uri: loc:IS-DAV

```
</details>

### Induced

<details>
```yaml
name: ISDAV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IS-DAV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Dalvíkurbyggð in country Iceland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IS-DAV
- Dalvíkurbyggð
exact_mappings:
- dpv_loc:IS-DAV
- dpv_loc_owl:IS-DAV
is_a: IS
class_uri: loc:IS-DAV

```
</details></div>