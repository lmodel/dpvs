---
search:
  boost: 10.0
---

# Class: ESBU 


_Concept representing region Province of Burgos in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-BU](https://w3id.org/lmodel/dpv/loc/ES-BU)





```mermaid
 classDiagram
    class ESBU
    click ESBU href "../ESBU/"
      ES <|-- ESBU
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESBU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-BU](https://w3id.org/lmodel/dpv/loc/ES-BU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-BU
* Province of Burgos




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-BU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-BU |
| native | loc:ESBU |
| exact | dpv_loc:ES-BU, dpv_loc_owl:ES-BU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESBU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-BU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Burgos in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-BU
- Province of Burgos
exact_mappings:
- dpv_loc:ES-BU
- dpv_loc_owl:ES-BU
is_a: ES
class_uri: loc:ES-BU

```
</details>

### Induced

<details>
```yaml
name: ESBU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-BU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Burgos in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-BU
- Province of Burgos
exact_mappings:
- dpv_loc:ES-BU
- dpv_loc_owl:ES-BU
is_a: ES
class_uri: loc:ES-BU

```
</details></div>