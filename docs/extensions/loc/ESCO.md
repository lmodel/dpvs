---
search:
  boost: 10.0
---

# Class: ESCO 


_Concept representing region Province of Córdoba, Spain in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CO](https://w3id.org/lmodel/dpv/loc/ES-CO)





```mermaid
 classDiagram
    class ESCO
    click ESCO href "../ESCO/"
      ES <|-- ESCO
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CO](https://w3id.org/lmodel/dpv/loc/ES-CO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CO
* Province of Córdoba, Spain




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CO |
| native | loc:ESCO |
| exact | dpv_loc:ES-CO, dpv_loc_owl:ES-CO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Córdoba, Spain in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CO
- Province of Córdoba, Spain
exact_mappings:
- dpv_loc:ES-CO
- dpv_loc_owl:ES-CO
is_a: ES
class_uri: loc:ES-CO

```
</details>

### Induced

<details>
```yaml
name: ESCO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Córdoba, Spain in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CO
- Province of Córdoba, Spain
exact_mappings:
- dpv_loc:ES-CO
- dpv_loc_owl:ES-CO
is_a: ES
class_uri: loc:ES-CO

```
</details></div>