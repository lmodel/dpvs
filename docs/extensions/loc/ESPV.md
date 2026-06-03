---
search:
  boost: 10.0
---

# Class: ESPV 


_Concept representing region Basque Autonomous Community in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-PV](https://w3id.org/lmodel/dpv/loc/ES-PV)





```mermaid
 classDiagram
    class ESPV
    click ESPV href "../ESPV/"
      ES <|-- ESPV
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESPV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-PV](https://w3id.org/lmodel/dpv/loc/ES-PV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-PV
* Basque Autonomous Community




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-PV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-PV |
| native | loc:ESPV |
| exact | dpv_loc:ES-PV, dpv_loc_owl:ES-PV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESPV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-PV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Basque Autonomous Community in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-PV
- Basque Autonomous Community
exact_mappings:
- dpv_loc:ES-PV
- dpv_loc_owl:ES-PV
is_a: ES
class_uri: loc:ES-PV

```
</details>

### Induced

<details>
```yaml
name: ESPV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-PV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Basque Autonomous Community in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-PV
- Basque Autonomous Community
exact_mappings:
- dpv_loc:ES-PV
- dpv_loc_owl:ES-PV
is_a: ES
class_uri: loc:ES-PV

```
</details></div>