---
search:
  boost: 10.0
---

# Class: ITMS 


_Concept representing region Province of Massa‑Carrara in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-MS](https://w3id.org/lmodel/dpv/loc/IT-MS)





```mermaid
 classDiagram
    class ITMS
    click ITMS href "../ITMS/"
      IT <|-- ITMS
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITMS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-MS](https://w3id.org/lmodel/dpv/loc/IT-MS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-MS
* Province of Massa‑Carrara




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-MS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-MS |
| native | loc:ITMS |
| exact | dpv_loc:IT-MS, dpv_loc_owl:IT-MS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITMS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Massa‑Carrara in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MS
- Province of Massa‑Carrara
exact_mappings:
- dpv_loc:IT-MS
- dpv_loc_owl:IT-MS
is_a: IT
class_uri: loc:IT-MS

```
</details>

### Induced

<details>
```yaml
name: ITMS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Massa‑Carrara in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MS
- Province of Massa‑Carrara
exact_mappings:
- dpv_loc:IT-MS
- dpv_loc_owl:IT-MS
is_a: IT
class_uri: loc:IT-MS

```
</details></div>