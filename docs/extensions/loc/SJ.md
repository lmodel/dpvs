---
search:
  boost: 10.0
---

# Class: SJ 


_Concept representing Country of Svalbard and Jan Mayen Islands_



<div data-search-exclude markdown="1">



URI: [loc:SJ](https://w3id.org/lmodel/dpv/loc/SJ)





```mermaid
 classDiagram
    class SJ
    click SJ href "../SJ/"
      NO <|-- SJ
        click NO href "../NO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NO](NO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md)]
        * **SJ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SJ](https://w3id.org/lmodel/dpv/loc/SJ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Svalbard and Jan Mayen Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SJ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SJ |
| native | loc:SJ |
| exact | dpv_loc:SJ, dpv_loc_owl:SJ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Svalbard and Jan Mayen Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Svalbard and Jan Mayen Islands
exact_mappings:
- dpv_loc:SJ
- dpv_loc_owl:SJ
is_a: 'NO'
class_uri: loc:SJ

```
</details>

### Induced

<details>
```yaml
name: SJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Svalbard and Jan Mayen Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Svalbard and Jan Mayen Islands
exact_mappings:
- dpv_loc:SJ
- dpv_loc_owl:SJ
is_a: 'NO'
class_uri: loc:SJ

```
</details></div>