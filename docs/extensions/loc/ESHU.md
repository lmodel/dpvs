---
search:
  boost: 10.0
---

# Class: ESHU 


_Concept representing region Province of Huesca in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-HU](https://w3id.org/lmodel/dpv/loc/ES-HU)





```mermaid
 classDiagram
    class ESHU
    click ESHU href "../ESHU/"
      ES <|-- ESHU
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESHU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-HU](https://w3id.org/lmodel/dpv/loc/ES-HU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-HU
* Province of Huesca




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-HU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-HU |
| native | loc:ESHU |
| exact | dpv_loc:ES-HU, dpv_loc_owl:ES-HU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESHU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-HU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Huesca in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-HU
- Province of Huesca
exact_mappings:
- dpv_loc:ES-HU
- dpv_loc_owl:ES-HU
is_a: ES
class_uri: loc:ES-HU

```
</details>

### Induced

<details>
```yaml
name: ESHU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-HU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Huesca in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-HU
- Province of Huesca
exact_mappings:
- dpv_loc:ES-HU
- dpv_loc_owl:ES-HU
is_a: ES
class_uri: loc:ES-HU

```
</details></div>